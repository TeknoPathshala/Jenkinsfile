pipeline {
    agent any
    environment {
        PATH = "${tool(name: 'venv', type: 'hudson.plugins.virtualenv.VirtualenvBuilder')}/bin:$PATH"
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Build and Test') {
            steps {
                script {
                    try {
                        sh 'python -m venv venv'
                        sh './venv/bin/activate'
                        sh 'pip install -r requirements.txt'
                        sh 'python your_script.py'
                    } finally {
                        sh 'deactivate'
                    }
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
            sh 'docker logout https://hub.docker.com'
        }
    }
}
