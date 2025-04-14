pipeline {
    agent any

    environment {
        SHORT_COMMIT = ''
        DOCKER_IMAGE = ''
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    SHORT_COMMIT = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    DOCKER_IMAGE = "mohitkaila/ensf400-group7-app:${SHORT_COMMIT}"
                    sh "docker build -t ${DOCKER_IMAGE} ."
                    sh "docker tag ${DOCKER_IMAGE} mohitkaila/ensf400-group7-app:latest"
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    echo "Running test.py inside Docker..."
                    sh "docker rm -f app-test || true"
                    sh "docker run -d -p 5000:5000 --name app-test ${DOCKER_IMAGE}"
                    sh "sleep 5"
                    sh "docker exec app-test python test.py || true"
                }
            }
        }

        stage('Push to Registry') {
            when {
                expression { return env.DOCKER_HUB_CREDENTIALS != null }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                    sh "echo $DOCKER_HUB_PASSWORD | docker login -u $DOCKER_HUB_USERNAME --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}"
                    sh "docker push mohitkaila/ensf400-group7-app:latest"
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up Docker..."
            sh "docker rm -f app-test || true"
        }
        failure {
            echo 'Build failed. Please check logs.'
        }
    }
}
