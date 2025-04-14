pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    SHORT_COMMIT=$(git rev-parse --short HEAD)
                    docker build -t mohitkaila/ensf400-group7-app:$SHORT_COMMIT .
                    docker tag mohitkaila/ensf400-group7-app:$SHORT_COMMIT mohitkaila/ensf400-group7-app:latest
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running test.py inside Docker...'
                sh '''
                    SHORT_COMMIT=$(git rev-parse --short HEAD)
                    docker rm -f app-test || true
                    docker run -d -p 5000:5000 --name app-test mohitkaila/ensf400-group7-app:$SHORT_COMMIT
                    sleep 5
                    docker exec app-test python test.py
                    docker stop app-test
                    docker rm app-test
                '''
            }
        }

        stage('Push to Registry') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                        echo "$PASSWORD" | docker login -u "$USERNAME" --password-stdin
                        SHORT_COMMIT=$(git rev-parse --short HEAD)
                        docker push mohitkaila/ensf400-group7-app:$SHORT_COMMIT
                        docker push mohitkaila/ensf400-group7-app:latest
                    '''
                }
            }
        }
    }

    post {
        failure {
            echo 'Build failed. Please check logs.'
        }
    }
}
