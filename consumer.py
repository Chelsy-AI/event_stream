import json
from confluent_kafka import Consumer

# Kafka setup
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'translator-group',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['translations'])

# Simple French → English dictionary
dictionary = {
    "Bonjour": "Hello",
    "Comment ça va?": "How are you?",
    "Je suis étudiant": "I am a student",
    "J'aime le chocolat": "I love chocolate",
    "Merci beaucoup": "Thank you very much"
}

print("🚀 Translator Consumer is running...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"❌ Consumer error: {msg.error()}")
        continue
    
    event = json.loads(msg.value().decode('utf-8'))
    french_text = event['french']
    english_text = dictionary.get(french_text, "[Translation not found]")
    
    print(f"🌐 French: {french_text} → English: {english_text}")
