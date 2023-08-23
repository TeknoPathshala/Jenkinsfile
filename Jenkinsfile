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
                        sh 'python3 -m venv venv'
                        sh './venv/bin/python -m pip install -r requirements.txt'
                        sh './venv/bin/python your_script.py'
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
                    def dockerImage = docker.build("my-ai-app:${env.BUILD_NUMBER}", 
                                    context: '.',       // Specify the context as the current directory
                                    dockerfile: 'Dockerfile')  // Specify the Dockerfile filename
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
