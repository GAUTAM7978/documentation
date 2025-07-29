
pipeline {
    agent any

    environment {
        IMAGE_NAME = "gautam6969/myip"
        DOCKER_CREDS = credentials('dockerid')  // Docker Hub credentials
        GIT_CREDS = credentials('github-token')  // Use credentials() for Git token
    }

    stages {
        stage('Checkout') {
            steps {
                git(
                    branch: 'main',
                    url: 'https://github.com/GAUTAM7978/documentation.git',
                    credentialsId: 'github-token'
                )
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:latest")
                }
            }
        }

       stage('Login to Docker Hub & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerid', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deploy.yaml'
                    sh 'kubectl apply -f k8s/service.yaml'
                    sh 'kubectl apply -f k8s/config.yaml'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
