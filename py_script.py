import pymongo
import datetime
import time

db_name = "weather_station"
table_name = "data"
client = pymongo.MongoClient(
    "mongodb+srv://test:test@cluster0.qwvki.mongodb.net/?retryWrites=true&w=majority",
)
my_db = client[db_name]
table = my_db[table_name]
while True:
    if table.find_one({"_id":1}) is not None:
        table.delete_one({"_id": 1})
    record = {
        "_id": 1,
        "temperature": 2,
        "pressure": 3,
        "humidity": 4,
        "date": datetime.datetime.now().isoformat(" ", "seconds")
    }
    table.insert_one(record)
    print(record)
    time.sleep(10)
