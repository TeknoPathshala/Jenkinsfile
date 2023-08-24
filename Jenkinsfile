pipeline {
    agent any
    environment {
        PATH = "$WORKSPACE/venv/bin:$PATH"
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
        stage('Run Flask Web Server') {
            steps {
                script {
                    sh 'venv/bin/python your_script.py &'
                }
            }
        }
    }
    post {
        always {
            script {
                sh 'pkill -f your_script.py'
            }
        }
    }
}
