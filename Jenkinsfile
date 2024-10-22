pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/LJHA10/Cody_Project'
            }
        }
        stage('Build') {
            steps {
                bat 'gradlew build'
            }
        }
        stage('Run Integration Tests') {
            steps {
                bat 'gradlew integrationTest'
            }
        }
        stage('Publish Results') {
            steps {
                junit '**/build/test-results/**/*.xml'
            }
        }
    }
}
