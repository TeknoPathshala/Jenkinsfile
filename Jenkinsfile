pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            steps {
                script {
                    def venv = virtualenv(
                        python: 'python3',
                        requirementsPath: 'requirements.txt'
                    )
                    sh "${venv}/bin/pip install -r requirements.txt"
                    sh "python your_script.py"
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'my-docker-credentials') {
                        def dockerImage = docker.build(context: '.', dockerfile: 'Dockerfile', tag: 'my-ai-app:27')
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'my-docker-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Your deployment steps here
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}

def virtualenv(Map configMap) {
    return tool name: 'venv', type: 'hudson.plugins.virtualenv.VirtualenvBuilder', properties: [
        $class: 'hudson.plugins.virtualenv.VirtualenvToolProperty', 
        locations: [
            [home: configMap['python']]
        ]
    ]
}
