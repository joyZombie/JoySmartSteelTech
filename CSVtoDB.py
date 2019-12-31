import pymongo
import os
import csv

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
"""dblist = myclient.list_database_names()"""
mydb = myclient["CSVdataDB"]
myColl = mydb["csvdata"]
myData = []

if os.path.isfile("task_data.csv"):
    with open("task_data.csv", "r") as filePtr:
        fileData = csv.DictReader(filePtr)
        for row in fileData:
            myData.append(row)
        """Clear the data and reupload"""
        myColl.delete_many({})
        print("Deleted old data")
        num = myColl.insert_many(myData)
        print("{0} new records inserted".format(len(num.inserted_ids)))
else:
    print("task_data.csv not found, exiting!!!")
