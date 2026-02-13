pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hemanth251/lab2-model"
    }

    stages {

        stage('Setup Python Environment') {
            steps {
                dir('lab2') {
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Application') {
            steps {
                dir('lab2') {
                    sh '''
                    . venv/bin/activate
                    python app.py
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('lab2') {
                    script {
                        docker.withRegistry('', 'dockerhub-creds') {
                            def app = docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}")
                            app.push()
                            app.push("latest")
                        }
                    }
                }
            }
        }
    }
}
