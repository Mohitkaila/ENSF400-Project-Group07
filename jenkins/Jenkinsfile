pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Mohitkaila/ENSF400_Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def commitHash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    def imageName = "mohitkaila/my-app:${commitHash}"
                    sh "docker build -t ${imageName} ."
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Installing necessary dependencies
                sh 'pip install requests'
                sh 'python3 test.py'
            }
        }

        stage('Push to Registry') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/']) {
                    script {
                        def commitHash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                        def imageName = "mohitkaila/my-app:${commitHash}"
                        sh "docker push ${imageName}"
                    }
                }
            }
        }
    }

    // To trigger the webhook manually, follow these steps:
    // 1. Push changes to the feature branch.
    // 2. Create a pull request to the main branch.
    // 3. This action should trigger the webhook and Jenkins should start building.
    // Check Jenkins logs for build details after the PR is created.

    // If the webhook isn't triggered, check GitHub Settings > Webhooks for issues or test the webhook again.
}
