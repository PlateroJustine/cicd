pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/PlateroJustine/cicd.git'
        GIT_CREDENTIALS_ID = 'github-pat'
        GIT_BRANCH = 'main'
        DEPLOY = '/var/www/html'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: "${GIT_BRANCH}",
                    url: "${GIT_REPO_URL}",
                    credentialsId: "${GIT_CREDENTIALS_ID}"
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                sudo apt-get update
                sudo apt-get install -y python3-venv python3-pip xvfb

                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Test') {
            steps {
                sh '''
                Xvfb :99 -screen 0 1024x768x16 &
                export DISPLAY=:99
                sleep 3

                . venv/bin/activate
                python test.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                sudo rsync -av --delete ./ ${DEPLOY}/
                sudo chown -R www-data:www-data ${DEPLOY}
                sudo chmod -R 755 ${DEPLOY}
                '''
            }
        }
    }

    post {
        success {
            echo "SUCCESS ✔"
        }
        failure {
            echo "FAILED ❌"
        }
        always {
            cleanWs()
        }
    }
}
