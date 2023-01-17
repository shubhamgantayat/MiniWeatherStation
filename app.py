from flask import render_template, jsonify, Flask, request
from flask_cors import cross_origin
import pymongo

app = Flask(__name__)
db_name = "weather_station"
table_name = "data"
client = pymongo.MongoClient(
    "mongodb+srv://test:test@cluster0.qwvki.mongodb.net/?retryWrites=true&w=majority",
)
my_db = client[db_name]
table = my_db[table_name]


@app.route('/')
@cross_origin()
def home_page():
    record = table.find_one({"_id": 1})
    return render_template(
        'form.html',
        temperature=record["temperature"],
        pressure=record["pressure"],
        humidity=record["humidity"],
        date=record["date"]
    )


if __name__ == '__main__':
    app.run(debug=True)
