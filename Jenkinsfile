pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Build stage: Setting up environment'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Test stage: Running tests'
                script {
                    def testExitCode = sh script: 'python -m unittest tests.py', returnStatus: true
                    if (testExitCode != 0) {
                        currentBuild.result = 'FAILURE'
                        error('Tests failed.')
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage: Cloning the program into local directory'
                sh 'mkdir tested_program'
                sh 'cd tested_program'
                sh 'curl -o main.py https://raw.githubusercontent.com/GuyShemesh66/Checkmarx_Home_Assignment/main/main.py'
            }
        }
    }

    post {
        failure {
            echo 'Pipeline failed: Tests did not pass.'
        }
        success {
            echo 'Pipeline succeeded: Tests passed and deployment completed.'
        }
    }
}
