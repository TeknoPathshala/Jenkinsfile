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
                    sh 'docker build -t my-ai-app:27 --file Dockerfile .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker run -d -p 8081:80 my-ai-app:27'
                }
            }
        }
    }
    post {
        always {
            script {
                sh 'docker ps -a'  // Show the list of running containers for verification
            }
        }
    }
}
