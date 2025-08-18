@Library('my-shared-lib') _

pipeline {
    agent any

    environment {
        IMAGE_NAME   = "gautam6969/myip"
        DOCKER_CREDS = 'dockerid'
        GIT_CREDS    = 'glpat-d7kNm_9tjKAHzqePraVdr286MQp1OmhmZXh5Cw.01.12071rg0v'
        GCP_CREDS    = 'gcp-service-account'
        PROJECT_ID   = "cloud-deployment-468004"
        CLUSTER_NAME = "my-gke-cluster"
        CLUSTER_ZONE = "us-central1-a"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://gitlab.com/GAUTAM7978/jenkins-shared-lib.git',
                    credentialsId: "${GIT_CREDS}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = buildDocker(IMAGE_NAME)
                }
            }
        }

        stage('Login & Push Docker Image') {
            steps {
                script {
                    pushDocker(IMAGE_NAME, DOCKER_CREDS)
                }
            }
        }

        stage('Authenticate to GKE') {
            steps {
                script {
                    authenticateGKE(PROJECT_ID, CLUSTER_NAME, CLUSTER_ZONE, GCP_CREDS)
                }
            }
        }

        stage('Deploy to GKE') {
            steps {
                script {
                    deployToK8s('k8s')
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully on GKE!'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
