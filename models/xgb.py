import xgboost as xgb

def train_xgb(X_train, y_train):
    model = xgb.XGBClassifier(
        n_estimators=100,
        max_depth=5,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8
    )
    model.fit(X_train, y_train)
    return model
