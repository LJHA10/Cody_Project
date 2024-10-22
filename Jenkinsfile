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
                bat 'python manage.py test myapp' // Reemplaza 'myapp' con el nombre de tu aplicación
            }
        }
    }

    post {
        always {
            junit '**/test-results.xml' // Asegúrate de que el archivo de resultados de pruebas esté disponible
        }
    }
}
