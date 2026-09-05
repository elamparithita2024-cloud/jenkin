pipeline {
    agent any

    stages {
        // Stage 1: Checkout Code
        stage('Checkout Code') {
            steps {
                // Clones/checkouts the GitHub repository automatically configured in Jenkins
                checkout scm
            }
        }

        // Stage 2: Build
        stage('Build') {
            steps {
                echo 'Executing Python application...'
               
                sh 'app.py'
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed.'
        }
    }
}
