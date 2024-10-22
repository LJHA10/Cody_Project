pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/LJHA10/Cody_Project'
            }
        }
        stage('Instalar Dependencias') {
            steps {
                bat 'conda activate py311 && pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                bat 'conda activate py311 && python manage.py test'
            }
        }
    }
}
