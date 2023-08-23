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
        stage('Setup Virtual Environment') {
            steps {
                script {
                    sh '''
                        virtualenv venv
                        source venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("my-image:${BUILD_NUMBER}")
                    docker.withRegistry('https://hub.docker.com', 'my-registry-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
        // Add more stages if needed
    }
    post {
        always {
            sh 'docker logout https://hub.docker.com'
            sh 'deactivate'
        }
    }
}
