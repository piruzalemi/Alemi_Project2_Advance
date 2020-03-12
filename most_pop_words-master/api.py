import pymongo
from flask import Flask, jsonify

#establish mongo connection 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["presidents"]

app = Flask(__name__)

@app.route("/api/v1/<presidents>")
def get_api_lang(presidents):
	data = list(db[presidents].find({}, {'_id': False}))
	return jsonify(data)

if __name__ == "__main__":
    app.run()