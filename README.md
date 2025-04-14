# ENSF400-Project-Group07

Project Overview

This project demonstrates the implementation of a complete CI/CD pipeline for a sample application, utilizing GitHub for source control, Docker for containerization, and Jenkins for automation. The pipeline ensures that every code change is automatically validated through container builds, unit tests, code quality checks, and end-to-end functional tests.

Technologies Used:

- Version Control: Git & GitHub
- Containerization: Docker
- Continuous Integration/Continuous Deployment: Jenkins
- Static Code Analysis: SonarQube
- Testing Framework: unittest (Python)

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

###

### Team Collaboration & Workflow
Throughout the development of this project, our team, Shalin, Mohit, and Rakshita followed a structured and collaborative approach to ensure smooth progress and maintain high code quality.

### Git Workflow
We adopted a GitHub-based workflow using the following practices:

Created feature branches for each task (features/shalin, feature/rakshita, etc.)

Used pull requests (PRs) for code review and merge discussions

Configured Jenkins webhooks to trigger automatic builds and analysis on every PR

Ensured all PRs passed Docker build, unit test, and SonarQube analysis before merging to main

### Task Distribution
Rakshita was responsible for setting up Jenkins in GitHub Codespaces, configuring GitHub webhooks, and managing CI pipeline jobs.

Mohit focused on containerizing the application using Docker, writing unit tests, and configuring the push to Docker Hub.

Shalin handled the integration of SonarQube, configured the quality gate, and ensured successful static analysis reporting in the pipeline.

### Coordination & Communication
Held weekly meetings to review progress and discuss blockers

Used a shared Google Doc to assign and track deliverables

Communicated daily via Discord for real-time collaboration and updates

Practiced pair programming for debugging critical pipeline issues

### Final Integration
Before the final check-in, the team regrouped to:

Perform a final pipeline walkthrough

Consolidate the Jenkinsfile into a unified, functional CI/CD script

Record a detailed video demonstration explaining each component and verifying that our implementation met all check-in requirements
