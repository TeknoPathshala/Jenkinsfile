pipeline {
    agent any
    environment {
        PATH = "$WORKSPACE/venv/bin:$PATH"
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh 'venv/bin/pip install -U pip'
                    sh 'venv/bin/pip install -r requirements.txt'
                }
            }
        }
        stage('Build and Test') {
            steps {
                script {
                    sh 'venv/bin/python your_script.py'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("my-ai-app:27", "--file Dockerfile .")
                    echo "Docker image built: ${dockerImage.id}"
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'my-registry-credentials', variable: 'DOCKER_LOGIN')]) {
                        sh "docker login -u $DOCKER_LOGIN -p $DOCKER_PASSWORD https://hub.docker.com"
                        sh 'docker push my-ai-app:27'
                    }
                }
            }
        }
        // Add more stages as needed...
    }
    post {
        always {
            sh 'docker logout https://hub.docker.com'
        }
    }
}
