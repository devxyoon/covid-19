from flask import Flask
import json
from backend.db_handler.mongodb_handler import MongoHandler

app = Flask(__name__)


@app.route('/korean_patient')
def korean_patient():
    mongodb = MongoHandler()
    find_items = list(mongodb.find_items(db_name="covid19", collection_name="korean_patients"))
    print(type(find_items))
    result = dict(zip(range(1, len(find_items) + 1), find_items))
    return json.dumps(result, default=str)


@app.route('/foreign_patient')
def foreign_patient():
    mongodb = MongoHandler()
    find_items = list(mongodb.find_items(db_name="covid19", collection_name="status_of_overseas_occurrence"))
    print(type(find_items))
    result = dict(zip(range(1, len(find_items) + 1), find_items))
    return json.dumps(result, default=str)


if __name__ == '__main__':
    app.run()
