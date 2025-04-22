#!/usr/bin/env python3
import json
import time
import random
from faker import Faker
from kafka import KafkaProducer

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = 'transactions'

def generate_transaction():
    return {
        'transaction_id': fake.uuid4(),
        'timestamp': fake.iso8601(),
        'transaction_status': random.choice(['success', 'failure']),
        'payment_status': (
            'charged' if random.random() < 0.9 else 'not_charged'
        ),
        'amount': round(random.uniform(1.0, 1000.0), 2),
        'customer_id': fake.uuid4()
    }

if __name__ == '__main__':
    print(f"Starting producer—publishing to topic “{TOPIC}”")
    while True:
        tx = generate_transaction()
        producer.send(TOPIC, value=tx)
        print(f"Sent: {tx}")
        time.sleep(1)
