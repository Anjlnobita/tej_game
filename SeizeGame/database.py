from motor import motor_asyncio
from pymongo import MongoClient

import config



#client 1 collection db url
Client_1 = motor_asyncio.asyncIOMotorClient(config.MONGO_DB_URI)
db_1 = Client_1["seize_collection"]

#client 2 coin update db url
Client_2 = motor_asynio.asyncIOMotorClient(config.MONGO_DB_UPDATE_URI)
db_2 = Client_2['Charector_catcher']

user_collection = db_2["user_collection_lmaoooo"]


#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
collection = db_1["charectors"]
nobita = db_1["users"]