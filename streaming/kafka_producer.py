from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda m: json.dumps(m).encode('utf-8')
)

transaction = {"amount": 250}

# Send and wait for acknowledgment
future = producer.send("transactions", transaction)
result = future.get(timeout=10)   # <-- wait for Kafka to confirm
print("Sent:", transaction)

producer.flush()
producer.close()
