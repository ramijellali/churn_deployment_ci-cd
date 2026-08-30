# Customer Churn Prediction — from notebook to deployed API

End-to-end ML pipeline on a telecom churn dataset: data preparation, benchmark of 7 classifiers,
serialized model, prediction API, Docker image and a GitHub Actions CI pipeline.

The point of this repo is not the model — it's the path from a notebook to something a business can actually call.

## Results

Seven algorithms trained and compared on the same split. Metrics are versioned in [`metrics.csv`](metrics.csv),
not buried in a notebook cell:

| Model | Accuracy | Precision | Recall | F1 | ROC AUC |
|---|---|---|---|---|---|
| **Random Forest** | **0.962** | 0.948 | 0.784 | **0.858** | 0.930 |
| XGBoost | 0.960 | 0.924 | 0.791 | 0.853 | **0.936** |
| Gradient Boosting | 0.955 | 0.914 | 0.763 | 0.831 | 0.932 |
| Decision Tree | 0.905 | 0.669 | 0.698 | 0.683 | 0.819 |
| KNN | 0.874 | 0.673 | 0.266 | 0.381 | 0.681 |
| Logistic Regression | 0.858 | 0.550 | 0.158 | 0.246 | 0.826 |
| SVM (RBF) | 0.854 | 0.000 | 0.000 | 0.000 | 0.754 |

Random Forest wins. Worth noting the failure case: the RBF SVM reaches 85 % accuracy while never
predicting a single churner — a reminder that accuracy alone is meaningless on imbalanced classes.

## Repository layout

| File | Role |
|---|---|
| `data_processing.py` | Loading, cleaning, encoding, train/test split |
| `train.py` | Trains the classifiers, writes `metrics.csv` and the serialized model to `models/` |
| `predict.py` | Loads the trained model and scores new records |
| `api.py` | Prediction endpoint |
| `deploy.py` | Deployment entry point |
| `Dockerfile` | Reproducible runtime |
| `.github/workflows/` | CI pipeline replayed on every push |
| `churn-bigml-80.csv` / `churn-bigml-20.csv` | Training and test data |

## Run it

```bash
pip install -r requirements.txt

python train.py        # trains, evaluates, writes metrics.csv + models/
python predict.py      # scores new records with the saved model
python api.py          # serves the prediction endpoint
```

With Docker:

```bash
docker build -t churn-api .
docker run -p 8000:8000 churn-api
```

## Where this pattern applies

The same skeleton — versioned metrics, a serialized model, an API, a container and a CI pipeline —
transfers to any business scoring problem: credit risk, fraud detection, lead prioritisation.

---

Built by [Rami Jellali](https://ramijellali.github.io) — AI engineer, Tunis. Available for freelance work.
