pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker-hub-credentials')
        GITHUB_WEBHOOK_SECRET = credentials('webhook-key')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    def commitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    sh "docker build -t mohitkaila/ensf400-group7-app:${commitId} ."
                    sh "docker tag mohitkaila/ensf400-group7-app:${commitId} mohitkaila/ensf400-group7-app:latest"
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running test.py against live Flask container...'
                script {
                    def commitId = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    sh "docker rm -f app-test || true"
                    sh "docker run -d -p 5000:5000 --name app-test mohitkaila/ensf400-group7-app:${commitId}"
                    sleep(time: 5, unit: 'SECONDS')
                    sh "docker exec app-test python3 test.py"
                    sh "docker rm -f app-test"
                }
            }
        }

        stage('SonarQube Analysis') {
            environment {
                scannerHome = tool 'SonarScanner'
            }
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=ensf400 -Dsonar.sources=. -Dsonar.python.version=3.9"
                }
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed. Check the logs above.'
        }
    }
}
