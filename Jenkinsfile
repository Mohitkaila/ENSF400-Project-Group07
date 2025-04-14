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
                    SHORT_COMMIT=$(echo $GIT_COMMIT | cut -c1-7)
                    docker build -t $DOCKER_HUB_USER/$IMAGE_NAME:$SHORT_COMMIT .
                    docker tag $DOCKER_HUB_USER/$IMAGE_NAME:$SHORT_COMMIT $DOCKER_HUB_USER/$IMAGE_NAME:latest
                '''
            }
        }

        stage('Run Unit Tests') {
    steps {
        echo 'Running test.py inside Docker...'
        sh '''
            SHORT_COMMIT=$(echo $GIT_COMMIT | cut -c1-7)
            docker run --rm mohitkaila/ensf400-group7-app:$SHORT_COMMIT python test.py
        '''
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
                        SHORT_COMMIT=$(echo $GIT_COMMIT | cut -c1-7)
                        docker push $DOCKER_HUB_USER/$IMAGE_NAME:$SHORT_COMMIT
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
