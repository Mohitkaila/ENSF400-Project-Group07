pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "mohitkaila/ensf400-group7-app"
    COMMIT_HASH = ""
  }

  stages {
    stage('Checkout Code') {
      steps {
        echo 'Checking out source code...'
        checkout scm
        script {
          COMMIT_HASH = sh(script: 'git rev-parse --short HEAD', returnStdout: true).trim()
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        echo 'Building Docker image...'
        script {
          sh """
            docker build -t $DOCKER_IMAGE:${COMMIT_HASH} .
            docker tag $DOCKER_IMAGE:${COMMIT_HASH} $DOCKER_IMAGE:latest
          """
        }
      }
    }

    stage('Run Unit Tests') {
      steps {
        echo 'Running test.py against live Flask container...'
        script {
          sh "docker rm -f app-test || true"
          sh "docker run -d -p 5000:5000 --name app-test $DOCKER_IMAGE:${COMMIT_HASH}"
          sleep time: 5, unit: 'SECONDS'
          sh "docker exec app-test python3 test.py"
          sh "docker stop app-test"
        }
      }
    }

    stage('Static Code Analysis') {
      environment {
        scannerHome = tool 'SonarScanner'
      }
      steps {
        echo 'Running SonarQube analysis...'
        withSonarQubeEnv('SonarQubeServer') {
          sh "${scannerHome}/bin/sonar-scanner"
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
