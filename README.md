### **`README.md`**

````markdown
# Kafka French → English Translator

This project is a real-time event streaming system built with **Apache Kafka** and **Python**.  
It demonstrates a **producer-consumer architecture** where French sentences are streamed from a producer to a consumer, which translates them into English in real-time.

---

## Features

- **Producer:** Sends French sentences as events to a Kafka topic `translations`.
- **Consumer:** Reads messages from Kafka and prints English translations.
- Real-time message flow using Kafka.
- Easily extendable to more languages or phrases.
- Optional continuous stream with automatic translation.

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone [your-repo-link]
cd event_stream
````

2. **Start Kafka with Docker Compose**

```bash
docker compose up -d
```

3. **Install Python dependencies**

Make sure you are in your virtual environment:

```bash
pip install -r requirements.txt
```

4. **Run the Producer**

```bash
python producer.py
```

5. **Run the Consumer** (in a separate terminal)

```bash
python consumer.py
```

You should see real-time translations like:

```
🌐 French: Bonjour → English: Hello
🌐 French: Merci beaucoup → English: Thank you very much
```

---

## Domain Description

* **Domain:** Language Translation
* **Events:** French sentences streamed in real-time
* **Consumer Use:** Translates French to English on-the-fly, useful for chat applications or learning platforms.

