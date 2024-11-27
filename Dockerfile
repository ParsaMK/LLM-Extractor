# Use an official Python runtime as the base image
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    bash \
    git \
    vim \
    curl 

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Open a bash shell by default
CMD [ "bash" ]

