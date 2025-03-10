pipeline {
    agent any

    stages {
        // Stage to install dependencies
        stage('Install Dependencies') {
            steps {
                script {
                    // Ensure pip is up-to-date and install pandas
                    sh 'pip install --upgrade pip'
                    sh 'pip install pandas'
                }
            }
        }

        // Stage for Data Processing
        stage('Data Processing') {
            steps {
                script {
                    // Run your data processing script
                    echo 'Starting Data Processing'
                    sh 'python3 data_processing.py'
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
