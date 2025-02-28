import mlflow
import mlflow.sklearn
import joblib
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from data_processing import load_data, preprocess_data

# Charger et prétraiter les données
df = load_data()
X, y, scaler, label_encoder = preprocess_data(df)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Liste des modèles à tester
models = {
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42),
    "SVM": SVC(probability=True, random_state=42),
    "DecisionTree": DecisionTreeClassifier(random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42)
}

# Set the experiment for MLflow
mlflow.set_experiment("mlops_project")

# Iterate through the models and train them
for name, model in models.items():
    with mlflow.start_run(run_name=name):

        # Train the model
        model.fit(X_train, y_train)

        # Make predictions
        y_pred = model.predict(X_test)

        # Compute accuracy
        accuracy = accuracy_score(y_test, y_pred)

        # Print model performance
        print(f"{name} Accuracy: {accuracy}")
        print(classification_report(y_test, y_pred))

        # Log metrics (accuracy) with MLflow
        mlflow.log_metric("accuracy", accuracy)

        # Log the trained model with MLflow
        mlflow.sklearn.log_model(model, f"{name}_model")

        # Optionally, log the parameters (e.g., n_estimators for RandomForest)
        if hasattr(model, 'n_estimators'):
            mlflow.log_param("n_estimators", model.n_estimators)

        # Save the model locally using joblib
        joblib.dump(model, f"{name}.pkl")
        print(f"Model {name} saved locally!")

# Note: Ensure you have the proper environment to view the MLflow UI, e.g.,
# running `mlflow ui --host 0.0.0.0 --port 5000` to visualize the logs.
