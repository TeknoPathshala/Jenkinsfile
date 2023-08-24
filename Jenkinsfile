pipeline {
    agent any
    environment {
        PATH = "$WORKSPACE/venv/bin:$PATH"
        DOCKER_REGISTRY_URL = 'https://hub.docker.com'  // Replace with your registry URL
    }
    stages {
        // ... Other stages ...

        stage('Build Docker Image') {
            steps {
                script {
                    def registryCreds = credentials('dckr_pat_CfOfgxvISm51upG5dWII9Ay5-CI')
                    withDockerRegistry(credentialsId: 'dckr_pat_CfOfgxvISm51upG5dWII9Ay5-CI', url: DOCKER_REGISTRY_URL) {
                        def customImage = docker.build("my-ai-app:27", "-f Dockerfile .")
                    }
                }
            }
        }

        // ... Other stages ...

        stage('Push Docker Image') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dckr_pat_CfOfgxvISm51upG5dWII9Ay5-CI', url: http://hub.docker.com) {
                        sh 'docker push my-ai-app:27'
                    }
                }
            }
        }
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
