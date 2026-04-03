import pandas as pd
import xgboost as xgb
import sys
sys.path.insert(0, '/home/vedant/Desktop/vs_code-project_folder/machine learning projects/fraud detection system')

from pipeline.feature_engineering import engineer_features
from pipeline.trainer import update_model

def test_online_learning():
    """Test incremental model update with new fraud patterns"""

    # Simulate new fraud transactions discovered
    new_transactions = pd.DataFrame({
        'src': [5, 12, 8],
        'dst': [15, 22, 19],
        'amount': [4500, 3800, 5200],
        'label': [1, 1, 1]  # All fraud
    })

    # Engineer features
    new_features = engineer_features(new_transactions)
    X_new = new_features[['mean_amount', 'total_amount', 'transaction_count']]
    y_new = new_features['label'] if 'label' in new_features else pd.Series([1]*len(X_new))

    print(f"New fraud patterns: {len(X_new)} accounts")
    print("Updating model with new fraud data...")

    try:
        update_model(X_new, y_new)
        print("✓ Online learning test PASSED - Model successfully updated")
        return True
    except Exception as e:
        print(f"✗ Online learning test FAILED: {e}")
        return False

if __name__ == "__main__":
    success = test_online_learning()
    sys.exit(0 if success else 1)
