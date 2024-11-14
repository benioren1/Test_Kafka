from flask import Blueprint , request
from pymongo import MongoClient
from collections import Counter

from db import session
from models.explos_model import Explos
from models.hostage_model import Hostage

MONGO_URI = 'mongodb://localhost:27017/'

DB_NAME = 'all_email'

COLLECTION_NAME = 'all_messages'

def get_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection

bp_query = Blueprint("query",__name__)

from flask import request, jsonify

@bp_query.route('/by_email',   methods=['GET'])
def get_all_messages_by_email():
    data = request.get_json()
    email = data['email']
    if not email:
        return jsonify({"error": "Email parameter is required"}), 400
    collection = get_collection()

    result = collection.find({"email": email})
    messages = []
    for message in result:
        message["_id"] = str(message["_id"])
        messages.append(message)


    return jsonify({"messages": messages}), 200


@bp_query.route("/by_froud_email", methods=["GET"])
def get_all_messages_by_forged_email():
    data = request.get_json()
    email1 = data['email']
    all_ho = session.query(Hostage).filter_by(email=email1)
    messages_ho = [message.to_dict() for message in all_ho]
    all_ex = session.query(Explos).filter_by(email=email1)
    messages_ex = [message.to_dict() for message in all_ex]
    return jsonify({"hostage_messages": messages_ho, "explos_messages": messages_ex}), 200





@bp_query.route("/world_by_email", methods=["GET"])
def get_all_messages_by_hostage_name():
    data = request.get_json()
    email = data["email"]
    my_dict = {}
    all_ho = session.query(Hostage).filter_by(email=email)
    messages_ho = [message.to_dict() for message in all_ho]
    all_ex = session.query(Explos).filter_by(email=email)
    messages_ex = [message.to_dict() for message in all_ex]
    all_messages = messages_ex + messages_ho
    sentences = [message['sentences'] for message in all_messages]
    tst = " ".join(sentences)
    cleaned_text = tst.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ')
    words = cleaned_text.split()
    for letter in words:
        if letter not in my_dict:
            my_dict[letter] = 0
        my_dict[letter] += 1
    return jsonify({"world_messages": my_dict}), 200


