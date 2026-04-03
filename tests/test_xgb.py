import numpy as np
from models.xgb import train_xgb

def test_xgb_training():
    # Dummy dataset
    X_train = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    y_train = np.array([0, 1, 0])

    model = train_xgb(X_train, y_train)
    preds = model.predict(X_train)

    assert len(preds) == len(y_train)
    assert set(preds).issubset({0, 1})
