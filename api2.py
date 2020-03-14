import pymongo
from flask import Flask, jsonify, render_template
from flask_cors import CORS



#establish mongo connection 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["presidents"]
collection=db.presidents_coordinates_poll

#app = Flask(__name__)
app = Flask(__name__, static_url_path='', static_folder="")
CORS(app)


@app.route("/api/v1/<presidents>")
def get_api_lang(presidents):
	#data = list(db[presidents].find({}, {'_id': False}))
    data = list(collection.find({}, {'_id': False}))
    #data = list(collection.find({"answer": "Sanders"}, {'_id': False}))
    #return jsonify(data)
    return jsonify(data)
    #return "12345"


@app.route("/") 
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()