pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Build stage: Setting up environment'
                sh 'pip install -r requirements.txt' // if we have libraries(numpy) we need to install for running our program
            }
        }

        stage('Test') {
            steps {
                echo 'Test stage: Running tests'
                script {
                    def testExitCode = sh script: 'python -m unittest tests.py', returnStatus: true  // check if the return string of our program is equal to "Hello World!"
                    if (testExitCode != 0) {
                        currentBuild.result = 'FAILURE'
                        error('Tests failed.')
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy stage: Clone the program into local file'
                sh 'mkdir tested_program'
                sh 'cd tested_program'
                sh 'curl -O https://raw.githubusercontent.com/GuyShemesh66/Checkmarx_Home_Assignment/main/main.py'
           }
        }
    }

    post {
        failure {
            echo 'Pipeline failed: Tests did not pass.'
        }
    }
}
