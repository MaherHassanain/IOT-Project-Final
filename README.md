# IOT-Project-Final
Smart Home Cooling/Heating System

---------------------------------------------------------------------------------------------------------------------------------------
1- Short description
- Broker.py starts broker and establishes connection with publishers/subscribers clients. Although connections are successful, subscribers fail to invoke the on_message method.
- Thermostat.py is an MQTT subscriber that monitors, and adjusts home temprature based on the smart home system model. The temprature is set based on FIFO entry priority inside the household.
- SmartDoorLocker.py is an MQTT publisher simulation of people enetring or leaving the house.
- ManagementApp.py is an MAQTT publisher that manages personel that are members of the household. It also allows view of household members and reset of members.

---------------------------------------------------------------------------------------------------------------------------------------
2-Software libraries

-  hbmqtt (https://hbmqtt.readthedocs.io/en/latest/).

-  paho-mqtt (https://pypi.org/project/paho-mqtt/).

-  asyncio (https://pypi.org/project/asyncio/).

-  pymongo (https://api.mongodb.com/python/current/installation.html).

---------------------------------------------------------------------------------------------------------------------------------------
3- OS information

-  Python program can be run by vriaty of OS including Windows and Linux systems. 

-  On Linux:
python versions 2.7.9+ or 3.4+ and corresponding pip.
pymongo version 3.10.1.
Supports MQTT protocol version 3.1 and 3.11.

-  on windows:
python version 3.8.1.
pip version 19.2.3.
pymongo version 3.10.1.

---------------------------------------------------------------------------------------------------------------------------------------
4- Required tools

Installing of libraries:
Windows: In terminal, on code directory where the program folder was cloned, write the following lines
1- pip3 install hbmqtt paho-mqtt asyncio (installs libraries to support for hbmqtt, paho-mqtt and asyncio)
2- python3 -m pip install pymongo (installs necessary libraries for the NoSQL)

---------------------------------------------------------------------------------------------------------------------------------------
5- How to run the programs
Windwows:
On terminal where the code directory is, three terminals need to be open for the whole programs to run:
First terminal
- python3 Thermostat.py
Second terminal
- python3 ManagementApp.py
Third terminal
- python3 SmartDoorLocker.py
Fourth terminal (not fully functional, but implemented)
- python3 Broker.py

To establish connection successfully to the broker instead of the open source broker used for the project, then:
1- Open program in any IDE
2- Find connect methods in Thermostat.pt, ManagementApp.py, and SmartDoorLocker.py, and comment them
3- Right below these methods, there are another commented connect method that connects to localhost broker and un-comment them
4- Run Broker.py, then run other programs 
