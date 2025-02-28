pipeline {
    agent any



    stages {
        stage('Data Processing') {
            steps {
                script {
                    echo "Starting Data Processing"
                    // Example: Run the data preprocessing script
                    sh 'python data_processing.py'
                }
            }
        }

        stage('Model Training') {
            steps {
                script {
                    echo "Starting Model Training"
                    // Example: Run the model training script
                    sh 'python train_model.py'
                }
            }
        }

        stage('Model Evaluation') {
            steps {
                script {
                    echo "Starting Model Evaluation"
                    // Example: Run the model evaluation script
                    sh 'python evaluate_model.py'
                }
            }
        }

        stage('Deploy Model') {
            when {
                expression {
                    // You can add conditions here to deploy the model if it passed evaluation
                    return currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                script {
                    echo "Deploying Model"
                    // Example: Deploy the model or save it
                    sh 'python deploy_model.py'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
