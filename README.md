Submitted by, Dipendu Gupta | 002010301042 | JU | Assignment Submission:

The "main.py" file is the main file whch takes the input.txt file, having the user inputs stored in a txt file (here this file is generated synthetically using the python script - "Generating Test Input files.py")
and generated the desired outputs , which is stored in the "output.txt" file. Now, this code is responsible for "Error Log Monitoring". According to the inputss , it generates the required output as mentioned in 
the question. For example - for input - "1 1715744138011; INTERNAL_SERVER_ERROR; 23.72 "  , the output will be - "No output" and so on having different case, as mentioned in the question.
The "requirements.txt" file is the list of required external libraries needed for executing the code. This "requirements.txt" file is also passed in the Dockerfile.

The Dockerfile📄:
The Dockerfile conatins the exectable steps for making the Docker image named "curieo_assignment".
The Dockerfile is executed and the container is run, this file (image and container), is uploaded in my DockerHub repository 👉 Link - https://hub.docker.com/r/dipendugupta/curieo_assignment/tags
The people who want to download/use the image in their system can use the folloing command to pull the image from my Docker REPO:
👉 docker pull dipendugupta/curieo_assignment:curieo_assignment
