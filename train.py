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

mlflow.set_experiment("mlops_project")

for name, model in models.items():
    with mlflow.start_run(run_name=name):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        print(f"{name} Accuracy: {accuracy}")
        print(classification_report(y_test, y_pred))

        # Log des métriques avec MLflow
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, f"{name}_model")

        # Sauvegarde du modèle
        joblib.dump(model, f"{name}.pkl")
        print(f"Modèle {name} sauvegardé localement !")