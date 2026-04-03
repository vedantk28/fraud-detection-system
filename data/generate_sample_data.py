import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Generate 1000 transactions
n_transactions = 1000
n_accounts = 50

# Create base transactions
src_accounts = np.random.choice(n_accounts, n_transactions)
dst_accounts = np.random.choice(n_accounts, n_transactions)

# Ensure src != dst
for i in range(n_transactions):
    while src_accounts[i] == dst_accounts[i]:
        dst_accounts[i] = np.random.randint(0, n_accounts)

# Generate amounts
amounts = np.random.exponential(1000, n_transactions)

# Generate timestamps
base_time = datetime.now() - timedelta(days=30)
timestamps = [base_time + timedelta(seconds=int(x)) for x in np.random.uniform(0, 30*86400, n_transactions)]

# Generate labels with fraud patterns (~30% fraud rate)
labels = np.zeros(n_transactions, dtype=int)

# Fraud patterns
fraud_accounts = np.random.choice(n_accounts, 12, replace=False)
for i in range(n_transactions):
    if np.random.random() < 0.30:  # 30% fraud rate
        labels[i] = 1

# Create DataFrame
df = pd.DataFrame({
    'src': src_accounts,
    'dst': dst_accounts,
    'amount': amounts,
    'timestamp': timestamps,
    'label': labels
})

# Save to CSV
df.to_csv('sample_transactions.csv', index=False)
print(f"Generated {len(df)} transactions")
print(f"Fraud cases: {df['label'].sum()} ({100*df['label'].sum()/len(df):.1f}%)")
print(df.head())
