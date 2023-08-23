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
                    docker.build("my-ai-app:27", context: ".", dockerfile: "Dockerfile")
                }
            }
        }
        // Other stages here...
    }
    post {
        always {
            sh 'docker logout https://registry.example.com'
        }
    }
}
