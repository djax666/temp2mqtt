#!/usr/bin/env python3
import paho.mqtt.publish as publish
import socket
from subprocess import check_output
from re import findall
from config import mqttserver

def get_temp():
    temp = check_output(["vcgencmd","measure_temp"]).decode("UTF-8")
    return(findall("\d+\.\d+",temp)[0])

def publish_message(topic, message):
    print("Publishing to MQTT topic: " + topic)
    print("Message: " + message)

    publish.single(topic, message,qos=1,retain=True, hostname=mqttserver)

def getmodel():
    model= "unknown"
    try:
        f = open('/proc/device-tree/model','r')
        model= (f.read())[:-1]
        f.close()
    except:
        model="unknown"

    return model

from datetime import datetime

# current date and time
curDT = datetime.now()
# current date and time
date_time = curDT.strftime("%Y-%m-%d %H:%M:%S")

temp = get_temp()
model= getmodel()
host= (socket.gethostname())

publish_message('homeassistant/sensor/raspberry/'+host+'_temperature/config','{"device":{"identifiers":["'+host+'"], "model":"'+model+'", "manufacturer":"Raspberry Pi Foundation", "name":"'+host+' CPU Temperature"}, "device_class": "temperature"   ,  "uniq_id":"'+host+'_temperature"    , "name": "'+host+' CPU Temperature", "state_topic": "Home/'+host+'/state", "unit_of_measurement": "°C", "value_template": "{{ value_json.temperature}}" }')

