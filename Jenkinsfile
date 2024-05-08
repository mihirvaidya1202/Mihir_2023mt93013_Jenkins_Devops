pipeline {
    agent any
  
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/mihirvaidya1202/Mihir_2023mt93013_Jenkins_Devops']]])
            }
        }
        
        stage('Build') {
            steps {
                sh 'python3 setup.py build'
            }
        }

        stage('Execute Python Script') {
            steps {
                sh 'python3 test.py'
            }
        }
    }
}
