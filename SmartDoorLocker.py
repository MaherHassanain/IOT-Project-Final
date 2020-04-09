
import paho.mqtt.client as mqttClient
import time
import datetime

def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Connected to broker")

        global Connected                #Use global variable
        Connected = True                #Signal connection

    else:

        print("Connection failed")

Connected = False   #global variable for the state of the connection

broker_address= "test.mosquitto.org"
port = 1883
# user = "yourUser"
# password = "yourPassword"

client = mqttClient.Client("Python1")               #create new instance
# client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)

try:
    while True:

    # string = raw_input("Input here:")
    # def token(string):
    #     start = 0
    #     i = 0
    #     token_list = []
    #     for x in range(0, len(string)):
    #         if " " == string[i:i+1][0]:
    #             token_list.append(string[start:i+1])
    #             #print string[start:i+1]
    #             start = i + 1
    #         i += 1
    #     token_list.append(string[start:i+1])
    #     return token_list
    #
    # print token(string)

        value = input('Enter Smart Door Results as name and 1/0. 1 means Enetred, 0 means left the house:')
        # res = value.split()
        client.publish("test/test",value)

except KeyboardInterrupt:

    client.disconnect()
    client.loop_stop()
