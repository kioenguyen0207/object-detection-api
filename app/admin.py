from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from bson.objectid import ObjectId

try:
    client = MongoClient("mongodb://db:27017")
    mydb = client['db']
    mycol = mydb['data']
except Exception as ex:
    print(f"ERROR :{ex}")

class classes(Resource):
    def get(self):
        if mycol.find_one() is None:
            file = open('detector/yolo/labels.txt', 'r')
            lines = file.readlines()
            for line in lines:
                value = {
                    "classname" : f"{line[:-1]}",
                    "status" : "accepted"
                }
                mycol.insert_one(value)
        ret = list(mycol.find())
        for val in ret:
            val["_id"] = str(val["_id"])
        return jsonify(ret)

    def post(self):
        postedData = request.get_json()
        bannedList = postedData['id']

        for _id in bannedList:
            query = {'_id': ObjectId(f"{_id}")}
            newValue = {"$set": {"status": "banned"}}
            mycol.update_one(query, newValue)
        
        ret = list(mycol.find())
        for val in ret:
            val["_id"] = str(val["_id"])
        return jsonify(ret)
    

if __name__ == "__main__":
    #clean up data in collection (renew labelmap)
    pass