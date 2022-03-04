from flask import Flask
import json
from flask import request
from services.database_service import DataBase
from config.config import config

app = Flask(__name__)
DataBase = DataBase(flask_app=app, param=config)


@app.route("/get", methods=['GET'])
def get():
    gender = request.args.get('gender')
    if gender:
        res = DataBase.get_by_gender(gender=gender)
        data = []
        for row in res:
            data.append(row.id)
        return json.dumps("There are {} {}s in this database".format(len(data), gender))
    else:
        res1 = DataBase.get_by_gender(gender="Male")
        res2 = DataBase.get_by_gender(gender="Female")
        data = []
        data2 = []
        for row in res1:
            data.append(row.id)
        for row in res2:
            data2.append(row.id)
        return json.dumps(
            "There are {} {}s and {} {}s in this database".format(len(data), "Male", len(data2), "Female"))


@app.route("/id", methods=['GET'])
def get_by_id():
    id = request.args.get('id', default=7)
    res = DataBase.get_by_id(id)
    if res:
        return json.dumps("The record with ID={} is {} years old".format(id, res.age))
    else:
        return json.dumps("No records with ID={}".format(id))


@app.route("/getall", methods=['GET'])
def get_all():
    res = DataBase.get_all()
    data = []
    for row in res:
        data.append(row.id)
    return json.dumps("There are a total of {} records in the dataset".format(len(data)))


@app.route("/delete", methods=['GET'])
def delete():
    id = request.args.get('id')
    if id:
        res = DataBase.delete_by_id(id=id)
        if res:
            return json.dumps("The record with ID={} has been deleted".format(id))
        else:
            return json.dumps("Error with id {}".format(id))
    else:
        return json.dumps("Please provide an ID to delete a record")


dummy_record = {'age': 25, 'attrition': 'Yes', 'business_travel': "Travel_Rarely", 'daily_rate': 5000,
                'distance_from_home': 5, 'education': "10", 'education_field': "ECE"}


@app.route("/insert", methods=['GET'])
def insert():
    record_id = DataBase.insert(dummy_record)
    return json.dumps("Record Inserted with id = {}".format(record_id))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
