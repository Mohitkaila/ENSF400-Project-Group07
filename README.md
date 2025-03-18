# ENSF400-Project-Group07

## ENSF 400 Project - CI/CD Pipeline

### Overview
This project integrates GitHub, Docker, and Jenkins for CI/CD automation.

### Git Workflow
1. *Branching*: Feature branches for development.
2. *Pull Requests*: All changes go through PRs before merging.
3. *Code Reviews*: At least one team member must approve a PR.

### How to Run the Project
```sh

# latest commit hash
COMMIT_HASH=$(git rev-parse --short HEAD)

# Build and run the image
docker build -t mohitkaila/my-app:$COMMIT_HASH .
docker run -p 5000:5000 mohitkaila/my-app:$COMMIT_HASH


### How to Run SonarQube
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts

If an existing docker container for SonarQube exists, it will give an error so run this command: 
docker stop sonarqube
docker rm sonarqube

After that, run this command again:-
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts 

The conatiner starts and lets us see port 9000 on browser. This port has our running SonarQube. 
We can access this manually too by running this: http://localhost:9000 on browser.
It should prompt you to see login page.