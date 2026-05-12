pipeline {
    agent any

    environment {
        // Define your Docker Hub credentials ID in Jenkins
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'
        DOCKER_IMAGE = 'yourusername/ai-travel-planner'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        // EKS Cluster details
        EKS_CLUSTER_NAME = 'ai-travel-planner-cluster'
        AWS_REGION = 'us-east-1'
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
                    echo "Building Docker Image: ${DOCKER_IMAGE}:${IMAGE_TAG}"
                    dockerImage = docker.build("${DOCKER_IMAGE}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo "Pushing Docker Image to Docker Hub..."
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKERHUB_CREDENTIALS}") {
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                script {
                    echo "Deploying to Kubernetes cluster ${EKS_CLUSTER_NAME}..."
                    // Update kubeconfig
                    sh "aws eks update-kubeconfig --region ${AWS_REGION} --name ${EKS_CLUSTER_NAME}"
                    
                    // Update deployment image using kubectl
                    sh """
                    kubectl set image deployment/ai-travel-planner flask-app=${DOCKER_IMAGE}:${IMAGE_TAG} --record
                    kubectl rollout status deployment/ai-travel-planner
                    """
                }
            }
        }
    }
    
    post {
        always {
            echo "Pipeline execution completed."
        }
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Deployment failed. Check the logs."
        }
    }
}
