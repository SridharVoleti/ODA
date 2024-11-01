pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/SridharVoleti/ODA.git', branch: 'jenkins'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    // Build images for both services
                    sh 'docker-compose -f ${COMPOSE_FILE} build'
                }
            }
        }

        stage('Run Services') {
            steps {
                script {
                    // Start the services in detached mode
                    sh 'docker-compose -f ${COMPOSE_FILE} up -d'
                }
            }
        }

        // stage('Integration Tests') {
        //     steps {
        //         script {
        //             // Run integration tests here, e.g., using curl to test endpoints
        //             sh '''
        //                 curl -f http://localhost:5000/health || exit 1
        //                 curl -f http://localhost:5001/health || exit 1
        //             '''
        //         }
        //     }
        //     post {
        //         always {
        //             // Log output if tests fail for debugging
        //             sh 'docker-compose logs'
        //         }
        //     }
        // }

        stage('Teardown') {
            steps {
                script {
                    // Stop and remove containers
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace after the pipeline run
            cleanWs()
        }
    }
}
