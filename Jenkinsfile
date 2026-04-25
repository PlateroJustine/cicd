pipeline {
    agent any

    environment {
        JAVA_HOME = "/opt/java17"
        DEPLOY = "/var/www/html"
        GIT_REPO_URL = 'https://github.com/PlateroJustine/cicd.git'
        GIT_CREDENTIALS_ID = 'github-pat'
        GIT_BRANCH = 'main'
    }

    stages {

        stage('Checkout SCM') {
            steps {
                echo "Checking out source code..."
                git branch: "${GIT_BRANCH}",
                    url: "${GIT_REPO_URL}",
                    credentialsId: "${GIT_CREDENTIALS_ID}"
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                set -x
                echo "Installing Python venv, pip, and Xvfb if missing..."
                sudo apt-get update
                sudo apt-get install -y python3-venv python3-pip xvfb

                echo "Creating virtual environment..."
                python3 -m venv venv
                . venv/bin/activate

                echo "Upgrading pip and installing requirements..."
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Start Apache') {
            steps {
                sh 'sudo systemctl start apache2'
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh '''
                set -x
                echo "Starting Xvfb for headless browser..."
                Xvfb :99 -screen 0 1024x768x16 &
                export DISPLAY=:99
                sleep 3

                echo "Running Selenium test..."
                . venv/bin/activate
                python test.py
                '''
            }
        }

        stage('Deploy to Apache') {
            steps {
                sh '''
                set -x
                echo "Deploying PHP project to Apache..."
                rsync -av --delete ./ ${DEPLOY}/
                sudo chown -R www-data:www-data ${DEPLOY}
                sudo chmod -R 755 ${DEPLOY}
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD SUCCESS ✔ Deployment completed"
        }
        failure {
            echo "CI/CD FAILED ❌ Check logs"
        }
        always {
            cleanWs()
        }
    }
}pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/PlateroJustine/cicd.git'
		GIT_CREDENTIALS_ID = 'github-pat'
        GIT_BRANCH = 'main'
        DEPLOY = '/var/www/html'
    }

    stages {

        stage('Checkout SCM') {
    steps {
        echo "Checking out source code..."
        git branch: 'main',
            url: 'https://github.com/PlateroJustine/cicd.git',
            credentialsId: 'github-pat'
    }
}

        stage('Setup Python Environment') {
            steps {
                sh '''
                set -x
                echo "Installing Python venv and pip if missing..."
                sudo apt-get update
                sudo apt-get install -y python3-venv python3-pip xvfb

                echo "Creating virtual environment..."
                python3 -m venv venv
                . venv/bin/activate

                echo "Upgrading pip and installing requirements..."
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh '''
                set -x
                echo "Starting Xvfb for headless browser..."
                Xvfb :99 -screen 0 1024x768x16 &
                export DISPLAY=:99
                sleep 3

                echo "Running Selenium test..."
                . venv/bin/activate
                python test.py
                '''
            }
        }

        stage('Deploy to Apache') {
            steps {
                sh '''
                set -x
                echo "Deploying PHP project to Apache..."

                sudo rsync -av --delete ./ ${DEPLOY}/
                sudo chown -R www-data:www-data ${DEPLOY}
                sudo chmod -R 755 ${DEPLOY}
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD SUCCESS ✔ Deployment completed"
        }
        failure {
            echo "CI/CD FAILED ❌ Check logs"
        }
        always {
            cleanWs()
        }
    }
}pipeline {
	agent any

    environment {
        JAVA_HOME = "/opt/java17"
        DEPLOY = "/var/www/html"
	}

	stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/PlateroJustine/cicd.git',
                    credentialsId: 'github-pat'
        	}
    	}

    	stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
        	}
    	}

        stage('Start Apache') {
            steps {
                sh 'sudo systemctl start apache2'
        	}
    	}

        stage('Test') {
            steps {
                sh '''
                . venv/bin/activate
                Xvfb :99 -screen 0 1024x768x16 &
                export DISPLAY=:99
                sleep 3
                python test.py
                '''
        	}
    	}

        stage('Deploy') {
            steps {
                sh '''
                rsync -av --delete ./ ${DEPLOY}/
                sudo chown -R www-data:www-data ${DEPLOY}
                sudo chmod -R 755 ${DEPLOY}
                '''
        	}
    	}
	}
}
