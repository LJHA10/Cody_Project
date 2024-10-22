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
                bat 'pip install django' // Instala Django si no está instalado
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                bat 'python manage.py test' // Ejecuta todas las pruebas
            }
        }
    }
}
