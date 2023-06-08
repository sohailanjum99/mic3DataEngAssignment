# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code to the container
COPY . .


# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the entrypoint command
ENTRYPOINT ["python", "app.py"]

