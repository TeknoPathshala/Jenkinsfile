pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Activate virtual environment if needed
                    sh 'source venv/bin/activate'

                    // Use sudo with Docker build command
                    sh 'sudo docker build -t my-ai-app:27 --file Dockerfile .'
                }
            }
        }

        // Add more stages for deployment, testing, etc.
    }

    post {
        always {
            // Deactivate virtual environment
            node {
                sh 'deactivate'
            }
        }
    }
}
