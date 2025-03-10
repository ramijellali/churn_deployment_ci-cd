pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Path to the virtual environment directory
    }

    stages {
        // Stage to set up the virtual environment and install dependencies
        stage('Setup Virtual Environment and Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python -m venv ${VENV_DIR}'

                    // Install dependencies inside the virtual environment
                    sh './${VENV_DIR}/Scripts/pip install --upgrade pip' // Upgrade pip in the virtual environment
                    sh './${VENV_DIR}/Scripts/pip install pandas' // Install pandas (add more packages if needed)
                }
            }
        }

        // Stage for Data Processing
        stage('Data Processing') {
            steps {
                script {
                    // Run your data processing script
                    echo 'Starting Data Processing'
                    sh './${VENV_DIR}/Scripts/python data_processing.py'
                }
            }
        }

        // Stage for Model Training (skipped if Data Processing fails)
        stage('Model Training') {
            steps {
                echo 'Model Training Stage Skipped due to earlier failure(s)'
            }
        }

        // Stage for Model Evaluation (skipped if previous stages fail)
        stage('Model Evaluation') {
            steps {
                echo 'Model Evaluation Stage Skipped due to earlier failure(s)'
            }
        }

        // Stage for Model Deployment (skipped if previous stages fail)
        stage('Deploy Model') {
            steps {
                echo 'Deploy Model Stage Skipped due to earlier failure(s)'
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
