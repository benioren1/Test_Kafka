from flask import Blueprint, request, jsonify
import json
from kafka import KafkaProducer


from services.servic_to_email import check_email, change_senteness

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)
bp_email = Blueprint('email', __name__)


@bp_email.route('/api/email', methods=['POST'])
def get_email():
    data = request.get_json()
    producer.send('topic_mes_all',value=data)
    print("send to message all")
    result = check_email(data)
    # print(result)
    new_data = change_senteness(data)
    if result == "hostage":
        producer.send('topic_hostage_1', value=new_data)
    if result == "explos":
        producer.send('topic_explos_1', value=new_data)



    # conn.commit()
    # conn.close()


    return jsonify({'message': 'Email sent successfully'}), 200
