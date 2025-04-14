pipeline {
    agent any

    environment {
        GITHUB_WEBHOOK_SECRET = credentials('webhook')
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials')
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
                echo "Running test.py inside Docker..."
                script {
                    def commitHash = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    sh "docker run --rm mohitkaila/ensf400-group7-app:${commitHash} python test.py"
                }
            }
        }

        stage('Push to Registry') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                script {
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                    def commitHash = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    sh "docker push mohitkaila/ensf400-group7-app:${commitHash}"
                    sh "docker push mohitkaila/ensf400-group7-app:latest"
                }
            }
        }

        stage('Debug Webhook Secret') {
            steps {
                echo "Webhook secret length: ${GITHUB_WEBHOOK_SECRET.length()}"
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully."
        }
        failure {
            echo "Pipeline failed. Check the logs above."
        }
    }
}
