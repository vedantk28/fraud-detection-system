import pandas as pd

def engineer_features(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Create simple statistical features for each account.
    """
    features = transactions.groupby('src').agg({
        'amount': ['mean', 'sum', 'count']
    })
    features.columns = ['mean_amount', 'total_amount', 'transaction_count']
    return features.reset_index()
