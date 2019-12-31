import pymongo
from flask import Flask
import datetime

app = Flask(__name__)
myClient = None
myDb = None
nyColl = None

@app.route("/",methods=['GET'])
@app.route("/index",methods=['GET'])
def getAllData():
    #Connect to DB
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
    myDb = myClient["CSVdataDB"]
    csvDataColl = myDb["csvdata"]
    appLogsColl = myDb["applogs"]
    #Log current time against each GET-request
    appLogsColl.insert_one({"type":"GET", "timestamp":datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")})
    #Return all data
    retData = []
    for row in csvDataColl.find():
        retData.append(row)
    return str(retData)
