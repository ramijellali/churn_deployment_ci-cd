pipeline {
    // Use your custom Docker image from Docker Hub
    agent {
        docker {
            image 'rjlali/api' // Your public Docker image
            args '-u root' // Run as root to avoid permission issues; adjust if needed
        }
    }

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
                    sh 'python3 -m venv ${VENV_DIR}' // Assumes python3; change to 'python' if needed

                    // Use bin/ for Unix-like systems (assuming your image is Linux-based)
                    sh './${VENV_DIR}/bin/pip install --upgrade pip'
                    sh './${VENV_DIR}/bin/pip install pandas'
                }
            }
        }

        // Stage for Data Processing
        stage('Data Processing') {
            steps {
                script {
                    echo 'Starting Data Processing'
                    sh './${VENV_DIR}/bin/python data_processing.py'
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