pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Create and activate virtual environment, then install dependencies
                    bat '''
                    python -m venv venv
                    .\\venv\\Scripts\\Activate
                    python -m pip install --upgrade pip
                    pip install pandas
                    '''
                }
            }
        }

        stage('Data Processing') {
            steps {
                script {
                    // Run your data processing script
                    echo 'Starting Data Processing'
                    bat '''
                    .\\venv\\Scripts\\Activate
                    python data_processing.py
                    '''
                }
            }
        }

        stage('Model Training') {
            steps {
                echo 'Model Training Stage Skipped due to earlier failure(s)'
            }
        }

        stage('Model Evaluation') {
            steps {
                echo 'Model Evaluation Stage Skipped due to earlier failure(s)'
            }
        }

        stage('Deploy Model') {
            steps {
                echo 'Deploy Model Stage Skipped due to earlier failure(s)'
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
