pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'apt update && apt upgrade -y'
                sh 'apt install python3 python3-pip -y'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test'){
            steps{
                sh 'pytest'
            }
        }
        stage('Deploy'){
            steps{
                sh 'python3 banking.py'
            }
        }
    }
}