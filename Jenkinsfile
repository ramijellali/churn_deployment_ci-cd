pipeline {
    agent any // Run on the default Jenkins node

    environment {
        VENV_DIR = 'venv' // Path to the virtual environment directory
    }

    stages {
        // Stage to verify Python installation
        stage('Test Verify Python Installation') {
            steps {
                script {
                    echo 'Checking Python installation...'
                    // Use bat for Windows commands; try both python and python3
                    bat 'where python || where python3 || echo Python not found'
                    bat 'python --version || python3 --version || echo No Python version available'
                }
            }
        }

        // Stage to set up the virtual environment and install dependencies
        stage('Setup Virtual Environment and Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment (use python3 or python based on availability)
                    bat 'python3 -m venv %VENV_DIR% || python -m venv %VENV_DIR%'

                    // Use Scripts for Windows virtual environment executables
                    bat '%VENV_DIR%\\Scripts\\pip install --upgrade pip'
                    bat '%VENV_DIR%\\Scripts\\pip install pandas'
                }
            }
        }

        // Stage for Data Processing
        stage('Data Processing') {
            steps {
                script {
                    echo 'Starting Data Processing'
                    bat '%VENV_DIR%\\Scripts\\python data_processing.py'
                }
            }
        }

        // Stage for Model Training
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

        // Stage for Model Evaluation
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

        // Stage for Model Deployment
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