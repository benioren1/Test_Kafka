# from sqlalchemy import SQLAlchemy
from pymongo import MongoClient
MONGO_URI = 'mongodb://localhost:27017/'

DB_NAME = 'all_email'

COLLECTION_NAME = 'all_messages'




def get_collection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection



# db = SQLAlchemy()

