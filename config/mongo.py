import os
from pymongo import MongoClient

MONGO_URL = os.environ.get(
    "MONGO_URL",
    "mongodb://admin:password@mongodb:27017/student_db?authSource=admin"
)

client = MongoClient(MONGO_URL)
db = client["student_db"]

student_collection = db["students"]
