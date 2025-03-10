pipeline {
    agent any // Run on the default Jenkins node (Linux)

    environment {
        VENV_DIR = 'venv' // Path to the virtual environment directory
    }

    stages {
        // Stage to verify Python installation
        stage('Test Verify Python Installation') {
            steps {
                script {
                    echo 'Checking Python installation...'
                    // Use sh for Linux; check python or python3
                    sh 'which python || which python3 || echo "Python not found"'
                    sh 'python --version || python3 --version || echo "No Python version available"'
                }
            }
        }

        // Stage to set up the virtual environment and install dependencies
        stage('Setup Virtual Environment and Install Dependencies') {
            steps {
                script {
                    // Try python3 first, fallback to python
                    sh 'python3 -m venv $VENV_DIR || python -m venv $VENV_DIR'
                    // Use bin/ for Linux virtual environment executables
                    sh './$VENV_DIR/bin/pip install --upgrade pip'
                    sh './$VENV_DIR/bin/pip install pandas'
                }
            }
        }

        // Stage for Data Processing
        stage('Data Processing') {
            steps {
                script {
                    echo 'Starting Data Processing'
                    sh './$VENV_DIR/bin/python data_processing.py'
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
                // Add your model training steps here (e.g., sh './$VENV_DIR/bin/python train_model.py')
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
                // Add your model evaluation steps here (e.g., sh './$VENV_DIR/bin/python evaluate_model.py')
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
                // Add your deployment steps here (e.g., sh './$VENV_DIR/bin/python deploy_model.py')
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