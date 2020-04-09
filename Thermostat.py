
import paho.mqtt.client as mqtt
import datetime
from pymongo import MongoClient
import time, threading

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database
db = conn.database
# Created or Switched to collection names: my_gfg_collection
collection = db.IOT


def display_db():
    for x in collection.find():
        print(x)
def insert_db(*var):
    # print("Entered db function")
    bad_chars = [';', ':', '!', "*", ']' , '[' , "'"]
    var = ''.join(i for i in var if not i in bad_chars)
    # print(var)
    length = len(var)-1
    # print(len(var))
    array = var[2:length]
    # print(array)
    currentLength = len(array)
    nameLength = currentLength-2
    arrayTempName = array[0:nameLength]
    numLength = len(arrayTempName)
    arrayTempTemp = array[numLength:len(array)]
    # print(arrayTempName)
    # print(arrayTempTemp)
    if arrayTempName == "sh":
        # show what is on DB
        for s in collection.find():
            print(s)
    elif arrayTempName == "dr":
        # deop DB
        collection.drop()
    else:
        # insert to DB
        x = datetime.datetime.now()
        print(x)
        variable = {
        "name" : arrayTempName,
        "temp" : arrayTempTemp,
        "inHouse" : 0,
        "datetime" : x
        }
        try:
            collection.insert_one(variable)
            print("Enter to DB successful")
            display_db()
        except:
            print("failed to enter to DB")

def update_inhouse_data(*var):
        # print("Entered db function")
        bad_chars = [';', ':', '!', "*", ']' , '[' , "'"]
        var = ''.join(i for i in var if not i in bad_chars)
        # print(var)
        length = len(var)-1
        # print(len(var))
        array = var[2:length]
        # print(array)
        currentLength = len(array)
        nameLength = currentLength-1
        arrayTempName = array[0:nameLength]
        numLength = len(arrayTempName)
        arrayTempBool = array[numLength:len(array)]
        # print(arrayTempName)
        # print(arrayTempBool)
        x = datetime.datetime.now()
        myquery = { "name": arrayTempName }
        newvalues = { "$set": { "inHouse": arrayTempBool } }
        newvalues1 = { "$set": { "datetime": x } }
        try:
            collection.update_one(myquery, newvalues)
        except:
            print("error in updating bool")
        try:
            collection.update_one(myquery, newvalues1)
        except:
            print("error in updating datetime")
        # try:
        #     collection.find({ "inHouse" : 1}).sort('datetime',-1)
        # except:
        #     print("error in date sorting")

def testfunc():
    print("test")
# var = ["khaled",3];
# emp_rec1 = {
#         "name":var[0],
#         "temp":var[1],
#         }
#
# rec_id1 = collection.insert_one(emp_rec1)
#
# cursor = collection.find()
# for record in cursor:
#     print(record)
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/test100")
    client.subscribe("test/test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    var = str(msg.payload)
    # print(msg.topic)
    tpc = msg.topic
    if tpc == "test/test":
        print("DOOR")
        try:
            update_inhouse_data(var)
        except:
            print("error occured")
    else:
        print("APP")
        # if var == "b'0'":
        #     print("In show condition")
        #     for x in collection.find():
        #         print(x)
        # elif var == 1:
        #     print("In drop condition")
        #     collection.drop()
        # else:
        try:
            # print("Inserting new member to DB")
            insert_db(var)
        except:
            print("error occured")


def timestamp_oldest(*args):
    min_ts = args[0]  # Set to first timestamp
    for arg in args[1:]:  # loop over remaining timestamps
        if arg < min_ts:
            min_ts = arg
    return datetime.datetime.fromtimestamp(min_ts)

def checkTargetTemprature():
    #initially temp is set to 15 degrees
    temp = 15
    myquery = { "inHouse": '1' }
    mydoc = collection.find(myquery)
    # for i in mydoc:
    #     print(i)
    #check how many are actually In house
    x = datetime.datetime.now()
    y = collection.count_documents({ "inHouse" : '1'})
    # x = mydoc.count()
    print("There is a total of ", y , " in the house. Time now is " , x)
    # print(x)
    if y == 0:
        print("Temprature set to 15 degrees")
        # threading.Timer(10, checkTargetTemprature).start()
    else:
        #need to decice who gets to set the temp based on
        # print("Temprature changes to a person preferance")
        # threading.Timer(10, checkTargetTemprature).start()
        # T = collection.find({"temp" : '22'}).sort({"datetime" : 1}).limit(1)
        # print(T)
        # oldest = datetime.datetime.now()
        # collection.find(myquery).sort()
        # print(mydoc)
        try:
            collection.find({ "inHouse" : 1}).sort('datetime',-1)
        except:
            print("error in date sorting")
            # print("Current time is")
        # allDates = mydoc['datetime']
        # print(allDates)
        # numberOfHomeMemembers = len(mydoc)
        # print(mydoc[0]['datetime'])
        array = []
        arrayTempTarget = []
        arrayNamesPriority = []
        indexNumber = 0
        for i in mydoc:
            dates = i['datetime']
            temps = i['temp']
            array.append(i['datetime'])
            arrayTempTarget.append(i['temp'])
            arrayNamesPriority.append(i['name'])
            # indexNumber++
            # print(i['name'])
            # print(i['datetime'])
        oldest = min(array)
        indexNumber = array.index(min(array))
        # print(oldest)
        # print(indexNumber)
        print("Temprature is set to " , arrayTempTarget[indexNumber] , " degrees celsius for " ,  arrayNamesPriority[indexNumber] , " since the individual has been in house since " , oldest)
        # print(arrayTempTarget[indexNumber])
        # for j in array:
        #     print(j)
            # print(i['temp'])
            # print('{0} {1}'.format(i['temp'], i['datetime']))
        # timestamp_oldest(dates)
        # targetDate = dates.min
        # for j in dates:
        #     print(j['datetime'])
        # print(dates.min)
        # for j in mydoc:
        #     if j['datetime'] == date.min:
        #         print(j['temp'])
        #         # indexNum = j
        #         # targetTemp = temps[1]
        # print("Temprature is set for")
        # print(temp[indexNum])
        # print(targetTemp)
    threading.Timer(10, checkTargetTemprature).start()


client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message

client.connect("test.mosquitto.org", port=1883)
#
# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# mydb = myclient['mydatabase']
# mycol = mydb["IOT"]

# mydict = { "name": "Maher", "temp": "33" }
#
# x = mycol.insert_one(mydict)

# print(myclient.list_database_names())
# print(mydb.list_collection_names())

# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="username",
#   passwd="password",
#   database="myDB"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE thermostat (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), temp INT(11), time DATETIME)")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
# mycol.drop()
# x = mycol.find_one()
# myquery = { "name": "Mr.Geek" }
#
# collection.delete_one(myquery)

# for x in mycol.find():
#   print(x)

# print(x)
# try:
#     collection.drop()
# except:
#     print("error in dropping")

while True:
    client.on_connect = on_connect
    client.on_message = on_message
    checkTargetTemprature()
    client.loop_forever()
