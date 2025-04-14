# ENSF400-Project-Group07

Project Overview
This project demonstrates the implementation of a complete CI/CD pipeline for a sample application, utilizing GitHub for source control, Docker for containerization, and Jenkins for automation. The pipeline ensures that every code change is automatically validated through container builds, unit tests, code quality checks, and end-to-end functional tests.

Technologies Used
Version Control: Git & GitHub

Containerization: Docker

Continuous Integration/Continuous Deployment: Jenkins

Static Code Analysis: SonarQube

Testing Framework: unittest (Python)

## Docker Image

This project is available as a Docker image on Docker Hub.

**Pull the image:**

```bash
docker pull mohitkaila/ensf400-group7-app
```

**Run the container:**

```bash
docker pull mohitkaila/ensf400-group7-app
```

---

## ENSF 400 Project - CI/CD Pipeline

### Overview

This project integrates GitHub, Docker, and Jenkins for CI/CD automation.

### Git Workflow

1. **Branching**: Feature branches for development  
2. **Pull Requests**: All changes go through PRs before merging  
3. **Code Reviews**: At least one team member must approve a PR

---

### How to Run the Project

Get the latest commit hash:

```bash
COMMIT_HASH=$(git rev-parse --short HEAD)
```

Build and run the image:

```bash
docker build -t mohitkaila/my-app:$COMMIT_HASH .
docker run -p 5000:5000 mohitkaila/my-app:$COMMIT_HASH
```

---

### How to Run SonarQube

Start SonarQube:

```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts
```

If a container already exists, stop and remove it:

```bash
docker stop sonarqube
docker rm sonarqube
```

Then restart SonarQube:

```bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts
```

Open your browser and go to:


```
http://localhost:9000
```

You should see the SonarQube login page.
