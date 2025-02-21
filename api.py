from fastapi import FastAPI
import numpy as np
from predict import predict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de prédiction du modèle ML!"}

@app.post("/predict/")
def make_prediction(model_name: str, features: list):
    try:
        prediction = predict(model_name, np.array(features))
        return {"model": model_name, "prediction": prediction}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
