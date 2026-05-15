pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ai-travel-planner"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                script {
                    echo "Building Docker image ${DOCKER_IMAGE}:${DOCKER_TAG}..."
                    bat "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                script {
                    echo "Deploying to Kubernetes..."
                    bat "kubectl apply -f k8s/manifests/"
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    echo "Verifying pods..."
                    bat "kubectl get pods"
                    bat "kubectl get svc"
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline finished."
        }
        success {
            echo "Deployment successful!"
        }
        failure {
            echo "Deployment failed."
        }
    }
}
