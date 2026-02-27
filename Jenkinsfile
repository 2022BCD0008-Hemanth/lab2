pipeline {
    agent any

    environment {
        IMAGE = "hemanth251/lab2-model:latest"
        CONTAINER = "wine_api_test"
    }

    stages {

        stage('Pull Image') {
            steps {
                echo "Pulling Docker image from DockerHub"
                sh 'docker pull $IMAGE'
            }
        }

        stage('Run Container') {
            steps {
                echo "Starting container"
                sh 'docker run -d -p 8000:8000 --name $CONTAINER $IMAGE'
            }
        }

        stage('Wait for API') {
            steps {
                script {
                    echo "Waiting for service readiness"
                    sleep 25
                }
            }
        }

        stage('Health Check') {
            steps {
                script {
                    def health = sh(
                        script: "curl -s http://localhost:8000/health",
                        returnStdout: true
                    ).trim()

                    echo "Health response: ${health}"

                    if (!health.contains("ok")) {
                        error("API did not start correctly")
                    }
                }
            }
        }

        stage('Valid Inference Request') {
            steps {
                script {
                    def response = sh(
                        script: "curl -s -X POST http://localhost:8000/predict -H 'Content-Type: application/json' -d @test_valid.json",
                        returnStdout: true
                    ).trim()

                    echo "Prediction response: ${response}"

                    if (!response.contains("wine_quality")) {
                        error("Prediction field missing!")
                    }
                }
            }
        }

        stage('Invalid Request Test') {
            steps {
                script {
                    def response = sh(
                        script: "curl -s -X POST http://localhost:8000/predict -H 'Content-Type: application/json' -d @test_invalid.json",
                        returnStdout: true
                    ).trim()

                    echo "Invalid response: ${response}"

                    if (!response.toLowerCase().contains("error") &&
                        !response.toLowerCase().contains("detail")) {
                        error("API failed to handle invalid input")
                    }
                }
            }
        }

        stage('Stop Container') {
            steps {
                sh 'docker stop $CONTAINER || true'
                sh 'docker rm $CONTAINER || true'
            }
        }
    }

    post {
        success {
            echo "MODEL VALIDATION PASSED"
        }
        failure {
            echo "MODEL VALIDATION FAILED"
        }
        always {
            sh 'docker rm -f $CONTAINER || true'
        }
    }
}