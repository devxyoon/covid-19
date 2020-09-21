from flask import Flask
import json
from db_handler.mongodb_handler import MongoHandler
from flask_cors import CORS

app = Flask(__name__)


@app.route('/korean_patient', methods=['GET'])
def korean_patient():
    mongodb = MongoHandler()
    find_items = list(mongodb.find_items(db_name="covid19", collection_name="korean_patients"))
    result = dict(zip(range(1, len(find_items) + 1), find_items))
    return json.dumps(result, default=str)


@app.route('/foreign_patient', methods=['GET'])
def foreign_patient():
    mongodb = MongoHandler()
    find_items = list(mongodb.find_items(db_name="covid19", collection_name="status_of_overseas_occurrence"))
    result = dict(zip(range(1, len(find_items) + 1), find_items))
    return json.dumps(result, default=str)


@app.route('/korea_news', methods=['GET'])
def korea_news():
    mongo = MongoHandler()
    find_items = list(mongo.find_items(db_name="covid19", collection_name="korea_news"))
    result = dict(zip(range(1, len(find_items) + 1), find_items))
    return json.dumps(result, default=str)


CORS(app)
if __name__ == '__main__':
    app.run()
