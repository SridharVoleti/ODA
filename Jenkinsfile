// pipeline {
//     agent any

//     environment {
//         COMPOSE_FILE = '/home/jenkins/docker-compose.yml'
//     }

//     stages {
//         stage('Clone Repository') {
//             steps {
//                 git url: 'https://github.com/SridharVoleti/ODA.git', branch: 'jenkins'
//             }
//         }

//         stage('Build Docker Images') {
//             steps {
//                 script {
//                     // Build images for both services
//                     sh 'docker-compose -f ${COMPOSE_FILE} build'
//                 }
//             }
//         }

//         stage('Run Services') {
//             steps {
//                 script {
//                     // Start the services in detached mode
//                     sh 'docker-compose -f ${COMPOSE_FILE} up -d'
//                 }
//             }
//         }

//         // stage('Integration Tests') {
//         //     steps {
//         //         script {
//         //             // Run integration tests here, e.g., using curl to test endpoints
//         //             sh '''
//         //                 curl -f http://localhost:5000/health || exit 1
//         //                 curl -f http://localhost:5001/health || exit 1
//         //             '''
//         //         }
//         //     }
//         //     post {
//         //         always {
//         //             // Log output if tests fail for debugging
//         //             sh 'docker-compose logs'
//         //         }
//         //     }
//         // }

//         stage('Teardown') {
//             steps {
//                 script {
//                     // Stop and remove containers
//                     sh 'docker-compose down'
//                 }
//             }
//         }
//     }

//     post {
//         always {
//             // Clean up workspace after the pipeline run
//             cleanWs()
//         }
//     }
// }


pipeline {
    agent any

    environment {
        TEMP_DIR = "${env.WORKSPACE}/temp"  // Use workspace directory for temp files
        COMPOSE_FILE = "${TEMP_DIR}/docker-compose.yaml"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/SridharVoleti/ODA.git', branch: 'jenkins'
                
                // Create a temporary directory in the Jenkins workspace and copy files
                sh "mkdir -p ${TEMP_DIR}"
                sh "cp -r Jenkinsfile MainApp MicroServices docker-compose.yaml ${TEMP_DIR}/"
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    // Use the copied docker-compose file in the workspace directory
                    sh "docker-compose -f ${COMPOSE_FILE} build"
                }
            }
        }

        stage('Run Services') {
            steps {
                script {
                    sh "docker-compose -f ${COMPOSE_FILE} up -d"
                }
            }
        }

        stage('Teardown') {
            steps {
                script {
                    sh "docker-compose -f ${COMPOSE_FILE} down"
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace and remove temporary directory
            cleanWs()
        }
    }
}
