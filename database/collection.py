from pymongo.collection import Collection
from pymongo.mongo_client import MongoClient
from config import MONGO_LOGIN, MONGO_PASS

uri = f"mongodb+srv://{MONGO_LOGIN}:{MONGO_PASS}@atlascluster.u3h56sm.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db: MongoClient = client.vapeshop
users_db: Collection = db.users
