pipeline {
    agent any

    environment {
        // Retrieve GitHub webhook secret from Jenkins credentials (ID: github-webhook-secret)
        GITHUB_WEBHOOK_SECRET = credentials('github-webhook-secret')
    }

    stages {
        stage('Checkout Code') {
            steps {
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
                // Add your test commands here
            }
        }

        stage('Push to Registry') {
            steps {
                echo "Pushing Docker image to registry..."
                script {
                    def commitHash = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    // Example: docker push (you might need to login before pushing)
                    sh "docker push mohitkaila/ensf400-group7-app:${commitHash}"
                }
            }
        }

        stage('Print Webhook Secret') {
            steps {
                echo "Webhook secret is: ${GITHUB_WEBHOOK_SECRET}" // For testing only – remove this line in production!
            }
        }
    }
}
