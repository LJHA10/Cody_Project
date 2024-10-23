<<<<<<< HEAD
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/LJHA10/Cody_Project.git'
            }
        }

        stage('Set Up Environment') {
            steps {
                script {
                    bat 'call C:\\Users\\luisj\\miniconda3\\Scripts\\activate.bat py311'
                    env.PATH = "C:\\Users\\luisj\\miniconda3\\envs\\py311\\Scripts;C:\\Users\\luisj\\miniconda3\\envs\\py311;$PATH"
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat 'pytest --junitxml=report.xml'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'report.xml'
            }
        }
    }

    post {
        always {
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
=======
>>>>>>> 6caac873f223060317557b22a78dc82ee82713b8
