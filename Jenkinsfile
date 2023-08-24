pipeline {
    agent none // Set to 'none' as you're using custom Docker image

    stages {
        stage('Checkout') {
            agent any // Use 'any' here to run on any available agent

            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            agent any // Use 'any' here to run on any available agent

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
