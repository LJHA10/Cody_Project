pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Instalar Dependencias') {
            steps {
                bat 'pip install django'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                bat 'python manage.py test'
            }
        }
    }
}
