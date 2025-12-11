import time
import uuid
import json
from confluent_kafka import Producer
import random

# Kafka setup
producer = Producer({'bootstrap.servers': 'localhost:9092'})
topic = "translations"

# Sample French phrases
french_phrases = [
    "Bonjour",
    "Comment ça va?",
    "Je suis étudiant",
    "J'aime le chocolat",
    "Merci beaucoup"
]

def delivery_report(err, msg):
    if err:
        print(f"❌ Message failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')} to {msg.topic()} : partition {msg.partition()} : offset {msg.offset()}")

print("🚀 Producer is running...")

# Send phrases in a loop
while True:
    phrase = random.choice(french_phrases)
    event = {
        "eventId": str(uuid.uuid4()),
        "french": phrase,
        "timestamp": int(time.time())
    }
    producer.produce(topic, value=json.dumps(event).encode('utf-8'), callback=delivery_report)
    producer.flush()
    time.sleep(2)  
