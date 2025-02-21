import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE


def load_data():
    """Charge les datasets et les fusionne si nécessaire."""
    df1 = pd.read_csv('churn-bigml-20.csv')
    df2 = pd.read_csv('churn-bigml-80.csv')
    df = pd.concat([df1, df2], ignore_index=True)
    return df


def preprocess_data(df):
    """Nettoie et transforme les données pour l'entraînement."""
    # Suppression des colonnes inutiles
    df.drop(columns=['State', 'Area code', 'Phone number'], inplace=True, errors='ignore')

    # Encodage des variables catégoriques
    le = LabelEncoder()
    df['Churn'] = le.fit_transform(df['Churn'])
    df = pd.get_dummies(df, drop_first=True)  # Encodage one-hot si besoin

    # Séparation des features et de la target
    X = df.drop(columns=['Churn'])
    y = df['Churn']

    # Standardisation des données
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Gestion du déséquilibre des classes
    smote = SMOTE()
    X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

    return X_resampled, y_resampled, scaler, le


if __name__ == "__main__":
    df = load_data()
    X, y, scaler, label_encoder = preprocess_data(df)
    print("Données préparées avec succès !")
