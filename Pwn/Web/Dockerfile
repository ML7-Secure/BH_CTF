# Use a base image, such as Ubuntu or Alpine Linux
FROM ubuntu:latest

# Install any necessary dependencies
RUN apt-get update && apt-get install -y curl

# Copy the executable into the container
COPY a.out /usr/local/bin/

# Set the default command to run the executable
CMD ["a.out"]
