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
    }
}
