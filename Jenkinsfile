pipeline {
    agent any

    environment {
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
                echo "Running test.py..."
                sh "python3 test.py"
            }
        }

        stage('Push to Registry') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    script {
                        def commitHash = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                        sh """
                            echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                            docker push mohitkaila/ensf400-group7-app:${commitHash}
                            docker push mohitkaila/ensf400-group7-app:latest
                        """
                    }
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
