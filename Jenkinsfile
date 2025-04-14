pipeline {
  agent any

  environment {
    IMAGE_NAME = 'mohitkaila/ensf400-group7-app'
    DOCKER_IMAGE = ''
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
          echo 'Building Docker image...'
          def commit = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
          env.DOCKER_IMAGE = "${IMAGE_NAME}:${commit}"
          sh """
            docker build -t ${DOCKER_IMAGE} .
            docker tag ${DOCKER_IMAGE} ${IMAGE_NAME}:latest
          """
        }
      }
    }

    stage('Run Unit Tests') {
      steps {
        script {
          echo 'Running test.py inside Docker...'
          sh '''
            docker rm -f app-test || true
            docker run -d -p 5000:5000 --name app-test ${DOCKER_IMAGE}
            sleep 5
            docker exec app-test python test.py || (docker logs app-test && exit 1)
          '''
        }
      }
    }

    stage('Push to Registry') {
      when {
        expression { currentBuild.currentResult == 'SUCCESS' }
      }
      steps {
        echo 'Pushing Docker image to Docker Hub...'
        withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push ${DOCKER_IMAGE}
            docker push ${IMAGE_NAME}:latest
          '''
        }
      }
    }
  }

  post {
    always {
      echo 'Cleaning up Docker...'
      sh 'docker rm -f app-test || true'
    }
    failure {
      echo 'Build failed. Please check logs.'
    }
  }
}
