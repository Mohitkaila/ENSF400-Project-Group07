# ENSF400-Project-Group07

## Docker Image

This project is available as a Docker image on Docker Hub.

**Pull the image:**
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
bash
Copy
Edit
# latest commit hash
COMMIT_HASH=$(git rev-parse --short HEAD)

# Build and run the image
docker build -t mohitkaila/my-app:$COMMIT_HASH .
docker run -p 5000:5000 mohitkaila/my-app:$COMMIT_HASH
How to Run SonarQube
bash
Copy
Edit
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts
If an existing docker container for SonarQube exists, stop and remove it:

bash
Copy
Edit
docker stop sonarqube
docker rm sonarqube
Then run SonarQube again:

bash
Copy
Edit
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts
Open your browser and go to:

arduino
Copy
Edit
http://localhost:9000
