pipeline {
    agent any
    environment {
        PATH = "$WORKSPACE/venv/bin:$PATH"
        DOCKER_REGISTRY_URL = credentials('my-registry-credentials')
        DOCKER_REGISTRY_CREDENTIALS = credentials('my-registry-credentials')
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
                    withCredentials([string(credentialsId: "${DOCKER_REGISTRY_CREDENTIALS}", variable: 'DOCKER_LOGIN'),
                                     string(credentialsId: "${DOCKER_REGISTRY_CREDENTIALS}", variable: 'DOCKER_PASSWORD')]) {
                        docker.withRegistry("${DOCKER_REGISTRY_URL}", "docker") {
                            def customImage = docker.build("my-ai-app:27", "-f Dockerfile .")
                        }
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'my-registry-credentials', variable: 'DOCKER_LOGIN'),
                                     string(credentialsId: 'my-registry-credentials', variable: 'DOCKER_PASSWORD')]) {
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
