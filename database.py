from pymongo import MongoClient
import certifi

ca = certifi.where()
MONGO_URI = ""


def db_connection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        new_db = client["db-regis"]
    except ConnectionError:
        print("connection error")
    return new_db
