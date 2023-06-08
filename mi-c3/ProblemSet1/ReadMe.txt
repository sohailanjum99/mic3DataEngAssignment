
####     HOW TO RUN   #####

1. Make sure you have Docker Daemon thread or DockerDesktop is running
2. Simple run the run.bat file present. It will make image by name time-difference
3. Now go to tool Like Postman 
    => Request Post   Url : http://localhost:8000/calculate_time_diff  
    => Body => Raw => Text :
        Sun 10 May 2015 13:54:36 -0700
        Sun 10 May 2015 13:54:36 -0000
        Sat 02 May 2015 19:54:36 +0530
        Fri 01 May 2015 13:54:36 -0000
        Sun 10 May 2015 13:54:36 -0700
        Sun 10 May 2015 13:54:36 -0000
        Sat 02 May 2015 19:54:36 +0530
        Fri 01 May 2015 13:54:36 -0000
    
4. on Send button the Response would be like 
            {
            "id": "<container id>",
            "result": [
                25200,
                88200,
                25200,
                88200
            ]
        }



Implementation:
Usling Python Flast API, I created the REST APi,

app.py => Method calculate_time_diff()
    this method received the list of string dates send in the body of post call from postman tool.
    Note :   one date should per line and must be in the format of "%a %d %b %Y %H:%M:%S %z"

app.py => Method Hello()
    this is Get call and on the dafault API path '/'
    To test the flask API is properly exposed and up, this method will return {"Hello" : "World"} dictionary

----===================================================-----

Dockerfile
    Provided info regarding python version, working dir and other configuration for docker image
    Please open Dockerfile in this directory and see comment at each line.

Requiremetns.txt 
    Contain the Module to be installed in Docker image, In our case we only required flask.