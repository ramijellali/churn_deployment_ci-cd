import joblib
import numpy as np
from data_processing import preprocess_data, load_data


# Charger le modèle souhaité (ex: RandomForest)
def load_model(model_name):
    return joblib.load(f"{model_name}.pkl")


# Fonction pour faire des prédictions
def predict(model_name, sample_data):
    model = load_model(model_name)

    # Charger les données pour récupérer le scaler et l'encoder
    df = load_data()
    _, _, scaler, label_encoder = preprocess_data(df)

    # Transformer les données d'entrée
    sample_data = scaler.transform([sample_data])
    prediction = model.predict(sample_data)

    return label_encoder.inverse_transform(prediction)[0]


if __name__ == "__main__":
    sample_input = np.random.rand(1, 10)  # Exemple de données aléatoires
    model_choice = "RandomForest"
    result = predict(model_choice, sample_input[0])
    print(f"Prédiction ({model_choice}):", result)
