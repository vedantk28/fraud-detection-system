import pandas as pd
import xgboost as xgb
from models.xgb import train_xgb
from pipeline.feature_engineering import engineer_features

def main():
    # Load transaction data
    transactions = pd.read_csv("data/sample_transactions.csv")
    print(f"Loaded {len(transactions)} transactions")
    print(f"Fraud rate: {transactions['label'].mean()*100:.1f}%")

    # Engineer features from source accounts
    features = engineer_features(transactions)
    print(f"Generated features for {len(features)} accounts")

    # Merge features with labels - take the label of first transaction from each src
    src_labels = transactions.groupby('src')['label'].first().reset_index()
    features = features.merge(src_labels, on='src')

    X = features[['mean_amount', 'total_amount', 'transaction_count']]
    y = features['label']

    print(f"Training XGBoost with {len(X)} samples...")
    model = train_xgb(X, y)
    model.save_model("models/fraud_xgb.json")
    print("✓ Model trained and saved to models/fraud_xgb.json")

def update_model(new_data: pd.DataFrame, new_labels: pd.Series):
    """Online learning: incrementally update model with new fraud patterns"""
    model = xgb.XGBClassifier()
    model.load_model("models/fraud_xgb.json")

    dtrain = xgb.DMatrix(new_data, label=new_labels)
    params = {"objective": "binary:logistic"}
    booster = xgb.train(params, dtrain, xgb_model=model.get_booster())

    booster.save_model("models/fraud_xgb.json")
    print("✓ Model updated with new fraud patterns!")

if __name__ == "__main__":
    main()

