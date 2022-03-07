from pymongo import MongoClient

try:
    client = MongoClient("mongodb://db:27017")
    mydb = client['db']
    mycol = mydb['data']
except Exception as ex:
    print(f"ERROR :{ex}")

def verify_classes(class_list):
    for item in class_list:
        if mycol.find_one({}, {"classname": f"{item}", "status": "banned"}) is not None:
            return "banned"
    return "accepted"

    