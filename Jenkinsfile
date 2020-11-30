pipeline {
    agent {
        docker {
            image 'devops_nodejs' 
            args '-p 6060:6060' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'npm install' 
            }
        }
    }
}