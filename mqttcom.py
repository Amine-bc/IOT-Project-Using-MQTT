#
# Copyright 2021 HiveMQ GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import mysql.connector
import paho.mqtt.client as paho
from paho import mqtt
from datetime import datetime


mydb = mysql.connector.connect(host="tiwsal.dz", user="user2022stg01", passwd="Nz2ck99$")
cursor = mydb.cursor()
# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5) #here in this line what is the Client attribute 
client.on_connect = on_connect
# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("4m1n3", "device1234")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("48f12ffbd3804fc1b5f9c592bfc5568e.s2.eu.hivemq.cloud", 8883)

# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish
# subscribe to all topics by using the wildcard "#"
client.subscribe("#", qos=1)
# The lines of code bellow aims to send the messages we want with non-stop 
while(1==1):
    content_msg=input('What do you want to publish ? ')
    obs_msg=input('which topic /*the root is testtopic*/ ')
    #a single publish, this can also be done in loops, etc.
    client.publish(obs_msg, payload=content_msg, qos=1)
    #Here save to the data base 
    datetime_msg = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    datap = [(content_msg, obs_msg, datetime_msg)]
    query ="insert into mqtt_sirius2022stg01.03amineb(content_msg, obs_msg, datetime_msg) values(%s, %s, %s) "
    #insert into mqtt_sirius2022stg01.01fethi(content_msg, obs_msg, datetime_msg) values(%s, %s, %s)
    #print(datetime_msg)
    cursor.executemany(query,datap)
    mydb.commit()
    #------------------------------
    #Here we print the DB content
    cursor.execute("select * from mqtt_sirius2022stg01.03amineb")
    result = cursor.fetchall()
    for data in result:
        print(data)
        
# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()
