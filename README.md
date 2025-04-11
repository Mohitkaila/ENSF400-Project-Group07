# ENSF400-Project-Group07

## Docker Image

This project is available as a Docker image on Docker Hub.

Pull the image:
```bash
docker pull mohitkaila/ensf400-group7-app
Run the container:

bash
Copy
Edit
docker run -p 5000:5000 mohitkaila/ensf400-group7-app
ENSF 400 Project - CI/CD Pipeline
Overview
This project integrates GitHub, Docker, and Jenkins for CI/CD automation.

Git Workflow
Branching: Feature branches for development.

Pull Requests: All changes go through PRs before merging.

Code Reviews: At least one team member must approve a PR.

How to Run the Project
sh
Copy
Edit
# latest commit hash
COMMIT_HASH=$(git rev-parse --short HEAD)

# Build and run the image
docker build -t mohitkaila/my-app:$COMMIT_HASH .
docker run -p 5000:5000 mohitkaila/my-app:$COMMIT_HASH
How to Run SonarQube
sh
Copy
Edit
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts
If an existing docker container for SonarQube exists, it will give an error so run this command:

sh
Copy
Edit
docker stop sonarqube
docker rm sonarqube
After that, run this command again:

sh
Copy
Edit
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts
The container starts and lets us see port 9000 on browser. This port has our running SonarQube.
We can access this manually too by running this: http://localhost:9000 on browser.
It should prompt you to see login page.