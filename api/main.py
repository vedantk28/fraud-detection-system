# api/main.py
from fastapi import FastAPI
import pandas as pd
import xgboost as xgb
import shap

app = FastAPI()

# Load trained model
model = xgb.XGBClassifier()
model.load_model("models/fraud_xgb.json")

# SHAP explainer
explainer = shap.TreeExplainer(model)

def engineer_features(transaction: dict) -> pd.DataFrame:
    df = pd.DataFrame([transaction])
    df['mean_amount'] = df['amount']
    df['total_amount'] = df['amount']
    df['transaction_count'] = 1
    return df[['mean_amount', 'total_amount', 'transaction_count']]

@app.post("/predict")
def predict(transaction: dict):
    X = engineer_features(transaction)
    prediction = model.predict(X)
    return {"fraud_prediction": int(prediction[0])}

@app.post("/explain")
def explain(transaction: dict):
    X = engineer_features(transaction)
    shap_values = explainer.shap_values(X)

    # Convert numpy.float32 → float
    explanation = {col: float(val) for col, val in zip(X.columns, shap_values[0])}

    prediction = model.predict(X)
    return {
        "fraud_prediction": int(prediction[0]),
        "explanation": explanation
    }

