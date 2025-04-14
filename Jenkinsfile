pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'mohitkaila'
        IMAGE_NAME = 'ensf400-group7-app'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t $DOCKER_HUB_USER/$IMAGE_NAME:${GIT_COMMIT::7} .
                    docker tag $DOCKER_HUB_USER/$IMAGE_NAME:${GIT_COMMIT::7} $DOCKER_HUB_USER/$IMAGE_NAME:latest
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest discover -s tests || true'
            }
        }

        stage('Push to Registry') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                withCredentials([usernamePassword(
                    credentialsId: 'docker-hub-credentials',
                    usernameVariable: 'USERNAME',
                    passwordVariable: 'PASSWORD'
                )]) {
                    sh '''
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                        docker push $DOCKER_HUB_USER/$IMAGE_NAME:${GIT_COMMIT::7}
                        docker push $DOCKER_HUB_USER/$IMAGE_NAME:latest
                    '''
                }
            }
        }
    }

    post {
        failure {
            echo 'Build failed. Please check logs.'
        }
        success {
            echo 'Build and push succeeded!'
        }
    }
}
