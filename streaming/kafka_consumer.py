from kafka import KafkaConsumer
import json
import requests
import psycopg2

# 🔑 Update this line with your new password
conn = psycopg2.connect(
    "dbname=fraud_detection user=vedant password=newpassword host=localhost"
)
cur = conn.cursor()

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    transaction = message.value
    response = requests.post("http://127.0.0.1:8000/predict", json=transaction)
    result = response.json()

    # Insert transaction into DB
    cur.execute(
        "INSERT INTO transactions (amount) VALUES (%s) RETURNING id;",
        (transaction["amount"],)
    )
    transaction_id = cur.fetchone()[0]

    # Insert prediction into DB
    cur.execute(
        "INSERT INTO predictions (transaction_id, fraud_prediction, shap_values) VALUES (%s, %s, %s);",
        (transaction_id, result["fraud_prediction"], json.dumps(result["explanation"]))
    )
    conn.commit()

    print("Transaction:", transaction, "Prediction:", result)
