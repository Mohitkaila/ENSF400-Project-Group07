# ENSF400-Project-Group07

# ENSF 400 Project - CI/CD Pipeline
## Overview
This project integrates GitHub, Docker, and Jenkins for CI/CD automation.

## Git Workflow
1. **Branching**: Feature branches for development.
2. **Pull Requests**: All changes go through PRs before merging.
3. **Code Reviews**: At least one team member must approve a PR.

## How to Run the Project
```sh
docker build -t my-app:v1 .
docker run -p 5000:5000 my-app:v1
