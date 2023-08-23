pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            steps {
                script {
                    try {
                        sh 'pip3 install -r requirements.txt'  // Install dependencies
                        sh 'python3 your_script.py'            // Execute the script
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        error("Build and test failed: ${e.getMessage()}")
                    }
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("my-ai-app:${env.BUILD_NUMBER}")
                }
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'docker-hub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    sh 'docker run -d -p 8080:80 my-ai-app:${env.BUILD_NUMBER}'
                }
            }
        }
    }
}
