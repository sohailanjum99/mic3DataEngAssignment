import pandas as pd
import numpy as np
import duckdb
import os

Root_folder_Path = os.getcwd()

# Read the CSV data into a DataFrame
df = pd.read_csv(f"{Root_folder_Path}\ProblemSet2\ipdr.csv")

# Convert the start time and end time columns to datetime with providing input format
df["starttime"] = pd.to_datetime(df["starttime"],format =  '%Y-%m-%d%H:%M:%S')
df["endtime"] = pd.to_datetime(df["endtime"],format =  '%Y-%m-%d%H:%M:%S')

# Calculate ET*(ET-10 min) for each FDR
df["endtime"] = np.where((df["endtime"] - pd.Timedelta(minutes=10)) < df["starttime"], df["endtime"], df["endtime"] - pd.Timedelta(minutes=10))

# Calculate the duration of each call in seconds
df["fdr_duration"] = (df["endtime"] - df["starttime"]).dt.total_seconds()

# Calculate the number of CDRs (fdr_count) to make a single call
df["fdr_count"] = df.groupby("msisdn")["msisdn"].transform("count")

# Calculate the total volume of each call of each domain in KB
df["total_volume"] = (df["dlvolume"] + df["ulvolume"]) #/ 1024

# Calculate the total time of each call of each VoIP App in seconds
df["total_time"] = (df.groupby(["msisdn", "domain"])["endtime"].transform(max) -
                    df.groupby(["msisdn", "domain"])["starttime"].transform(min)).dt.total_seconds()

# Calculate the bit rate (kbps) of each call of each VoIP App
df["bit_rate"] = df["total_volume"] / df["total_time"]

# Identification of audio or video call 
df["isAudio"] = np.where( (df["bit_rate"] >10) & (df["bit_rate"] <= 400)   , True, False)
df["isVideo"] = np.where(df["bit_rate"] > 200, True, False)


dfcalls = duckdb.query(""" select df.*, row_number() over ( partition by msisdn order by domain ) as call_Nb 
from df  
order by msisdn, domain """).df()

# Select the desired columns for the output,  I added an addition column Call
output = dfcalls[["msisdn", "domain", "fdr_duration", "fdr_count", "bit_rate", "isAudio", "isVideo",'call_Nb']]

output.to_csv(f"{Root_folder_Path}\ProblemSet2\ETL_output.csv" , header=True, index=False )
