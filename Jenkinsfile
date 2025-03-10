pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
    }
    stages {
        stage('Test Verify Python Installation') {
            steps {
                script {
                    echo 'Checking Python installation...'
                    sh 'which python3 || echo "Python3 not found"'
                    sh 'python3 --version || echo "No Python3 version available"'
                }
            }
        }
        stage('Setup Virtual Environment and Install Dependencies') {
            steps {
                script {
                    sh 'python3 -m venv $VENV_DIR'
                    sh './$VENV_DIR/bin/pip install --upgrade pip'
                    sh './$VENV_DIR/bin/pip install pandas'
                }
            }
        }
        stage('Data Processing') {
            steps {
                script {
                    echo 'Starting Data Processing'
                    sh './$VENV_DIR/bin/python data_processing.py'
                }
            }
        }
        stage('Model Training') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Running Model Training...'
            }
        }
        stage('Model Evaluation') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Running Model Evaluation...'
            }
        }
        stage('Deploy Model') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Deploying Model...'
            }
        }
        stage('Post Actions') {
            steps {
                echo 'Pipeline finished. Please check the logs.'
            }
        }
    }
    post {
        always {
            echo 'Pipeline has completed.'
        }
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for errors.'
        }
    }
}