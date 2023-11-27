pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/carpachecus/novatec.git']])
            }
        }
    
        stage('test') {
            steps {
                 sh 'pytest test_launch.py'
            }
        }
        stage('Sonar Analysis') {
            environment {
                scannerHome = tool 'sonarqube5'
            }
            steps {
               withSonarQubeEnv('sonarqube') {
                   sh '''${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=carpachecus_novatec \
                   -Dsonar.organization=carpachecus '''    
                }
            }
        }
        stage('Build and Push') {
            steps {
                script {
                        docker.withRegistry('https://index.docker.io/v1/', 'docker-id') {

                        def dockerImage = docker.build("carpachecus/appserver-python:${env.BUILD_ID}")

                        dockerImage.push()

                    }
                }	
            }        
        }
    }   
}
