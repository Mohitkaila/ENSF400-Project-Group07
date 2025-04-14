pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Mohitkaila/ENSF400_Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def commitHash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                    def imageName = "mohitkaila/my-app:${commitHash}"
                    sh "docker build -t ${imageName} ."
                }
            }
        }

        stage('Push to Registry') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub', url: 'https://index.docker.io/v1/']) {
                    script {
                        def commitHash = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
                        def imageName = "mohitkaila/my-app:${commitHash}"
                        sh "docker push ${imageName}"
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        curl -sSLo sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
                        unzip sonar-scanner.zip
                        mv sonar-scanner-* sonar-scanner
                        cd sonarqube && ../sonar-scanner/bin/sonar-scanner
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
