pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Path to the virtual environment directory
    }

    stages {
        // Stage to verify Python installation
        stage('Test Verify Python Installation') {
            steps {
                script {
                    echo 'Checking Python installation...'
                    // Check for python or python3 and their versions
                    sh 'which python || which python3 || echo "Python not found"'
                    sh 'python --version || python3 --version || echo "No Python version available"'
                }
            }
        }

        // Stage to set up the virtual environment and install dependencies
        stage('Setup Virtual Environment and Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment with python3
                    sh 'python3 -m venv ${VENV_DIR}'

                    // Use appropriate path for pip based on OS
                    if (isUnix()) {
                        sh './${VENV_DIR}/bin/pip install --upgrade pip'
                        sh './${VENV_DIR}/bin/pip install pandas'
                    } else {
                        sh './${VENV_DIR}/Scripts/pip install --upgrade pip'
                        sh './${VENV_DIR}/Scripts/pip install pandas'
                    }
                }
            }
        }

        // Stage for Data Processing
        stage('Data Processing') {
            steps {
                script {
                    echo 'Starting Data Processing'
                    if (isUnix()) {
                        sh './${VENV_DIR}/bin/python data_processing.py'
                    } else {
                        sh './${VENV_DIR}/Scripts/python data_processing.py'
                    }
                }
            }
        }

        // Stage for Model Training (skipped if Data Processing fails)
        stage('Model Training') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Running Model Training...'
                // Add your model training steps here
            }
        }

        // Stage for Model Evaluation (skipped if previous stages fail)
        stage('Model Evaluation') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Running Model Evaluation...'
                // Add your model evaluation steps here
            }
        }

        // Stage for Model Deployment (skipped if previous stages fail)
        stage('Deploy Model') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                echo 'Deploying Model...'
                // Add your deployment steps here
            }
        }

        // Post actions after pipeline execution
        stage('Post Actions') {
            steps {
                echo 'Pipeline finished. Please check the logs.'
            }
        }
    }

    post {
        // Cleanup or notify after pipeline completion
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