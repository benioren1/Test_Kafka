import json

from kafka import KafkaConsumer, KafkaProducer
import time

#
consumer_p = KafkaConsumer(
    'topic_explos_1',
    bootstrap_servers='localhost:9092',  # broker
    group_id='group_message',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Consumer started, waiting for messages...")

for message in consumer_p:
    message_str = message
    print(f"Consumer_P received message: {message}")

    try:
        consumer_p.commit()
        print("Offset committed successfully.")
    except Exception as e:
        print(f"Error committing offset: {e}")

    time.sleep(1)
