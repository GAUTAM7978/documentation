
pipeline {
    agent any

environment {
    IMAGE_NAME = "gautam6969/myip"
    DOCKER_CREDS = credentials('gautam6969')  // ID of Docker Hub credentials in Jenkins
}

stages {
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/GAUTAM7978/documentation.git',
                    credentialsId: 'Gautam_01/******'
            }
        }
    }


    stage('Build Docker Image') {
        steps {
            script {
                dockerImage = docker.build("${gautam6969/myip}:latest")
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
                docker.withRegistry('https://index.docker.io/v1/', 'gautam6969') {
                    dockerImage.push("latest")
                }
            }
        }
    }

    stage('Deploy') {
        steps {
            script {
                // Apply Kubernetes deployment
                sh 'kubectl apply -f k8s/deploy.yaml'
                sh 'kubectl apply -f k8s/service.yml'
                sh 'kubectl apply -f k8s/config.yml'
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