pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = "mohitkaila"
    }

    stages {
        stage('Build Docker Image') {
    steps {
        echo 'Building Docker image...'
        sh 'docker build -t mohitkaila/ensf400-group7-app:latest .'
    }
}


        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest test.py'
            }
        }

        stage('Push to Registry') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        COMMIT_HASH=$(git rev-parse --short HEAD)
                        docker push $DOCKER_HUB_USER/ensf400-group7-app:$COMMIT_HASH
                    '''
                }
            }
        }
    }
}
