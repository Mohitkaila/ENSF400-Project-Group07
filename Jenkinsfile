pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials')
        GITHUB_WEBHOOK_SECRET = credentials('webhook')
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                script {
                    def commitHash = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    sh "docker build -t mohitkaila/ensf400-group7-app:${commitHash} ."
                    sh "docker tag mohitkaila/ensf400-group7-app:${commitHash} mohitkaila/ensf400-group7-app:latest"
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running test.py against live Flask container..."
                script {
                    def commitHash = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    sh "docker rm -f app-test || true"
                    sh "docker run -d -p 5000:5000 --name app-test mohitkaila/ensf400-group7-app:${commitHash}"
                    sleep 5
                    sh "docker exec app-test python3 test.py"
                    sh "docker rm -f app-test"
                }
            }
        }

        stage('Push to Registry') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                script {
                    def commitHash = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                    sh "docker push mohitkaila/ensf400-group7-app:${commitHash}"
                    sh "docker push mohitkaila/ensf400-group7-app:latest"
                }
            }
        }

        stage('Debug Webhook Secret') {
            steps {
                echo "Webhook secret loaded."
                echo "Length: ${GITHUB_WEBHOOK_SECRET.length()}"
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed. Check the logs above."
        }
        success {
            echo "Pipeline executed successfully."
        }
    }
}
