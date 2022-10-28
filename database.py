import os
from pymongo import MongoClient
import certifi
from dotenv import load_dotenv

load_dotenv()

ca = certifi.where()

DB_USER = os.getenv("DB_USER")
BD_PASS = os.getenv("BD_PASS")
MONGO_URI = f"mongodb+srv://{DB_USER}:{BD_PASS}@cluster0.6cs6zuz.mongodb.net/?retryWrites=true&w=majority"


def db_connection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        new_db = client["db-regis"]
    except ConnectionError:
        print("connection error")
    return new_db
