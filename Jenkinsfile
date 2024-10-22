pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/LJHA10/Cody_Project.git'
            }
        }
        stage('Build') {
            steps {
                sh './gradlew build'
            }
        }
        stage('Run Integration Tests') {
            steps {
                sh './gradlew integrationTest'
            }
        }
        stage('Publish Results') {
            steps {
                junit '**/build/test-results/**/*.xml'
            }
        }
    }
}
