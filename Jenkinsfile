
pipeline {
    agent any

    environment {
        IMAGE_NAME = "gautam6969/myip"
        DOCKER_CREDS = credentials('gautam6969')  // Docker Hub credentials
        GIT_CREDS = 'Gautam_01'  // Corrected Git credentials ID (no slash)
    }

    stages {
        stage('Checkout') {
            steps {
                git(
                    branch: 'main',
                    url: 'https://github.com/GAUTAM7978/documentation.git',
                    credentialsId: "${GIT_CREDS}"
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

        stage('Run Unit Tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest tests || echo "No tests found."'
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKER_CREDS) {
                        dockerImage.push("latest")
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deploy.yaml'
                    sh 'kubectl apply -f k8s/service.yml'
                    sh 'kubectl apply -f k8s/config.yml'
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
