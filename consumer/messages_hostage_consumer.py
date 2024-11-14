from kafka import KafkaConsumer, KafkaProducer
import time

# Consumer קבלת הודעות מהנושא
consumer_p = KafkaConsumer(
    'topic_hostage',
    bootstrap_servers='localhost:9092',  # broker
    group_id='group_message',
    auto_offset_reset='earliest',
    enable_auto_commit=False
)

print("Consumer started, waiting for messages...")

for message in consumer_p:
    message_str = message.value.decode('utf-8')
    print(f"Consumer_P received message: {message.value.decode('utf-8')}")

    try:
        consumer_p.commit()
        print("Offset committed successfully.")
    except Exception as e:
        print(f"Error committing offset: {e}")

    time.sleep(1)
