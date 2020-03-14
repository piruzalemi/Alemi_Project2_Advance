import pymongo
from flask import Flask, jsonify
from flask_cors import CORS
## import sys
## from __future__ import print_function

## print('Hello world!', file=sys.stderr)


#establish mongo connection 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["presidents"]
collection=db.presidents_coordinates_poll

app = Flask(__name__)
CORS(app)


@app.route("/api/v1/<presidents>")
def get_api_lang(presidents):
	#data = list(db[presidents].find({}, {'_id': False}))
    data = list(collection.find({}, {'_id': False}))
    return jsonify(data)
    #return "12345"

if __name__ == "__main__":
    app.run()