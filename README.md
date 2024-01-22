# Flask App Docker Deployment

This guide walks you through the steps to deploy a Flask application using Docker. The Flask app includes a home route that returns "Hello World".

## Prerequisites

- Docker installed on your machine.


## Application Details

- Home Route: The Flask app contains a home route (`/`) that, when accessed, will display "Hello World".

## Steps to Deploy

1. Pull the Docker Image

   First, pull the image `chethanpss24/flask_app:1.0.0` from the Docker repository:

   docker pull chethanpss24/flask_app:1.0.0
 

2. Run the Docker Container

   Use the following command to run the Docker container. Replace `<ur_machine_port>` with the port number you want to use on your machine, and `your_container_name` with a name of your choice for the container.

   
   docker run -d -p <ur_machine_port>:5000 --name your_container_name chethanpss24/flask_app:1.0.0
   

   For example, if you want to expose the Flask app on port 8080 on your machine, the command will be:

   
   docker run -d -p 8080:5000 --name my_flask_app chethanpss24/flask_app:1.0.0
   

3. Accessing the Flask App

   After running the container, you can access the Flask app by navigating to `http://localhost:<ur_machine_port>` in your web browser. Replace `<ur_machine_port>` with the port number you used in the run command.

   - Access the home route: Navigate to `http://localhost:<ur_machine_port>/` to see the "Hello World" message.

4. Stopping the Container

   To stop the running Docker container, use the command:

   
   docker stop your_container_name
   

   Replace `your_container_name` with the name you assigned to your container.

## Additional Commands

- To list all running containers:

  
  docker ps
  

- To list all containers, including stopped ones:

  
  docker ps -a
  

- To remove a stopped container:

  
  docker rm your_container_name
  