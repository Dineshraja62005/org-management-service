from pymongo import MongoClient

# MongoDB connection URL (local)
MONGO_URL = "mongodb://localhost:27017"

# Create Mongo client
client = MongoClient(MONGO_URL)

# Master database
db = client["org_master_db"]

# Master collection for organizations
org_collection = db["organizations"]
