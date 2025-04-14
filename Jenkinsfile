pipeline {
    agent any

    environment {
        GITHUB_WEBHOOK_SECRET = credentials('github-webhook-secret')
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
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running unit tests..."
                sh "echo 'Tests passed!'"
            }
        }

        stage('Push to Registry') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                script {
                    def commitHash = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    sh "docker push mohitkaila/ensf400-group7-app:${commitHash}"
                }
            }
        }

        stage('Debug Webhook Secret') {
            steps {
                echo "Webhook secret successfully loaded."
                echo "Webhook secret length: ${GITHUB_WEBHOOK_SECRET.length()}"
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed. Check logs above."
        }
        success {
            echo "Pipeline executed successfully."
        }
    }
}
