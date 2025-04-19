pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                dir('e-commerce-app') {
                    bat 'python -m venv venv'
                    bat 'call .\\venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                dir('e-commerce-app') {
                    bat '''
                        call .\\venv\\Scripts\\activate
                        set PYTHONPATH=%cd%
                        pytest tests\\
                    '''
                }
            }
        }

        stage('Docker Build') {
            steps {
                dir('e-commerce-app') {
                    sh 'docker build -t momo777yazilim/e-commerce-app:latest .'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop e-commerce-app || true'
                sh 'docker rm e-commerce-app || true'
                sh 'docker run -d -p 5000:5000 --name e-commerce-app momo777yazilim/e-commerce-app:latest'
            }
        }
    }
}
