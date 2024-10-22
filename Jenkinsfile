pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Hacemos un checkout del repositorio
                    git url: 'https://github.com/LJHA10/Cody_Project'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    // Llama a gradlew build, asegurándote de que la ruta sea correcta
                    bat 'gradlew build'
                }
            }
        }
        stage('Run Integration Tests') {
            steps {
                script {
                    // Ejecuta las pruebas de integración
                    bat 'gradlew integrationTest'
                }
            }
        }
        stage('Publish Results') {
            steps {
                script {
                    // Publica los resultados de las pruebas
                    junit '**/build/test-results/**/*.xml'
                }
            }
        }
    }
    post {
        always {
            // Siempre se ejecuta, incluso si la compilación falla
            echo 'Cleaning up...'
            cleanWs() // Limpia el espacio de trabajo
        }
        success {
            // Se ejecuta solo si el pipeline tiene éxito
            echo 'Pipeline completed successfully!'
        }
        failure {
            // Se ejecuta solo si el pipeline falla
            echo 'Pipeline failed!'
        }
    }
}
