pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clona el repositorio
                git 'https://github.com/LJHA10/Cody_Project.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                script {
                    // Activa el entorno de Conda
                    bat 'call C:\\Users\\luisj\\miniconda3\\Scripts\\activate.bat py311'
                    // Establece el PATH para pytest
                    env.PATH = "C:\\Users\\luisj\\miniconda3\\envs\\py311\\Scripts;C:\\Users\\luisj\\miniconda3\\envs\\py311;$PATH"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Ejecuta pytest
                    bat 'pytest --junitxml=report.xml'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                // Publica los resultados de las pruebas
                junit 'report.xml'
            }
        }
    }

    post {
        always {
            // Acciones que se ejecutan siempre, como limpiar el workspace
            cleanWs()
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
