pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        GITHUB_WEBHOOK_SECRET = credentials('webhook')
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
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
                    def COMMIT_HASH = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    sh "docker build -t mohitkaila/ensf400-group7-app:${COMMIT_HASH} ."
                    sh "docker tag mohitkaila/ensf400-group7-app:${COMMIT_HASH} mohitkaila/ensf400-group7-app:latest"
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running test.py inside Docker..."
                script {
                    def COMMIT_HASH = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    sh "docker run --rm mohitkaila/ensf400-group7-app:${COMMIT_HASH} python test.py"
                }
            }
        }

        stage('Push to Registry') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                script {
                    def COMMIT_HASH = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                        sh "docker push mohitkaila/ensf400-group7-app:${COMMIT_HASH}"
                        sh "docker push mohitkaila/ensf400-group7-app:latest"
                    }
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
        failure {
            echo "Pipeline failed. Check the logs above."
        }
        success {
            echo "Pipeline executed successfully."
        }
    }
}
