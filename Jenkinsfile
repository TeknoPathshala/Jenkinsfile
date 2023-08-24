pipeline {
    agent any
    environment {
        PATH = "$WORKSPACE/venv/bin:$PATH"
        DOCKER_REGISTRY_URL = 'https://hub.docker.com'  // Replace with your registry URL
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
                    def registryCreds = credentials('dckr_pat_CfOfgxvISm51upG5dWII9Ay5-CI')
                    withDockerRegistry(credentialsId: 'dckr_pat_CfOfgxvISm51upG5dWII9Ay5-CI', url: 'https://hub.docker.com') {
                        def customImage = docker.build("my-ai-app:27", "-f Dockerfile .")
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dckr_pat_CfOfgxvISm51upG5dWII9Ay5-CI', url: 'https://hub.docker.com') {
                        def customImage = docker.build("my-ai-app:27", "-f Dockerfile .")
                        customImage.push()
                    }
                }
            }
        }
        // Add more stages as needed...
    }
    post {
        always {
            // ... Other post actions ...
            script {
                sh 'docker logout https://hub.docker.com'
            }
        }
    }
}
