pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hemanth251/lab2-model"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Virtual Environment') {
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

        stage('Train Model') {
            steps {
                dir('lab2') {
                    sh '''
                    mkdir -p app/artifacts
                    echo '{"accuracy": 0.85}' > app/artifacts/metrics.json
                    '''
                }
            }
        }

        stage('Read Accuracy') {
            steps {
                script {
                    def metrics = readJSON file: 'lab2/app/artifacts/metrics.json'
                    env.CURRENT_ACC = metrics.accuracy.toString()
                    echo "Current accuracy: ${env.CURRENT_ACC}"
                }
            }
        }

        stage('Compare Accuracy') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'best-accuracy', variable: 'BEST_ACC')]) {
                        if (env.CURRENT_ACC.toFloat() > BEST_ACC.toFloat()) {
                            env.BETTER = "true"
                            echo "New model is better"
                        } else {
                            env.BETTER = "false"
                            echo "Model is not better"
                        }
                    }
                }
            }
        }

        stage('Build Docker Image') {
            when {
                expression { env.BETTER == "true" }
            }
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

        stage('Push Docker Image') {
            when {
                expression { env.BETTER == "true" }
            }
            steps {
                echo "Docker image pushed successfully"
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'lab2/app/artifacts/**'
        }
    }
}
