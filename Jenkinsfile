pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/LJHA10/Cody_Project' // Cambia a tu repositorio
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt' // Instala dependencias
            }
        }
        
        stage('Run Integration Tests') {
            steps {
                bat 'pytest' // Ejecuta las pruebas de integración
            }
        }
    }
    
    post {
        always {
            junit '**/test-results/**/*.xml' // Publica resultados, ajusta según tu configuración
        }
    }
}
