import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
)

def pablish_email(email_data):
    email = json.dumps(email_data)
    producer.send('topic_hostage',value=email)
    print(f"Email sent to Kafka")






    producer.flush()
    # סיום העבודה עם המפיק
    producer.close()