pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clona el repositorio
                git 'https://github.com/LJHA10/Cody_Project' // Cambia a tu repositorio
            }
        }

        stage('Install Python and Dependencies') {
            steps {
                // Instala Python y las dependencias del proyecto
                bat 'python -m pip install --upgrade pip' // Actualiza pip
                bat 'pip install -r requirements.txt' // Instala dependencias
            }
        }

        stage('Run Tests') {
            steps {
                // Ejecuta las pruebas de Django
                bat 'python manage.py test myapp > result.log; type result.log' // Ejecuta tests y muestra resultados
            }
        }
    }

    post {
        always {
            // Publica resultados si hay archivos XML de JUnit (ajusta según sea necesario)
            junit '**/test-results/*.xml' // Publica resultados si tienes archivos XML de resultados
        }
    }
}
