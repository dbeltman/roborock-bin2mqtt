import json
import os
import paho.mqtt.publish as mqtt_publish
import paho.mqtt.client as mqtt
from templates import binsensor
from components import ssh_controller

mqtt_host = os.getenv('MQTTHOST', 'MQTT-Server')
mqtt_port = os.getenv('MQTTPORT', 1883)
mqtt_username = os.getenv('MQTTUSERNAME', 'iot')
mqtt_password = os.getenv('MQTTPASSWORD', 'changeme')
mqtt_client_name = os.getenv('MQTTCLIENTNAME', 'bin2mqtt')

device_name = os.getenv('DEVICENAME', 'roborock')
binsensor_config_topic = os.getenv('DISCOTOPIC', 'homeassistant/sensor/' + binsensor.binsensor_name + '/config')
mqtt_binsensor_topic = binsensor.binsensor_topic

def publish(topic, payload):
    print("Publishing {}'".format(payload)) 
    print("TO TOPIC {}".format(topic))
    try:
        mqtt_publish.single(topic, payload,
                        hostname=mqtt_host,
                        client_id=mqtt_client_name,
                        port=mqtt_port,
                        retain=True,
                        auth={'username':mqtt_username, 'password':mqtt_password})
    except:
        print("ERROR: Something went wrong publishing '" + str(payload) + "' to topic '" + str(topic) + "'!")
        exit(1)

def publish_config():
    # try:       
    print("Publishing binsensor config")
    publish(binsensor_config_topic, json.dumps(binsensor.binsensor_config_template))
    # except:
    #     print("Something went wrong publishing configs to discovery topic!")
def publish_metrics():
    # try:
    metric="bin-empty-date"
    print("Publishing metric " + metric)
    publish(mqtt_binsensor_topic, str(ssh_controller.get_metrics()))
    # except:
    #     print("Something went wrong publishing metric " + metric)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))
    # try:
    #     client.subscribe(mqtt_subscribe_topics)
    #     # print("Connected to MQTT.")
    # except:
    #     print("ERROR: Something went wrong subscribing to " + str(mqtt_subscribe_topics))

def init_connect():
    try:
        print("Connecting to MQTT Server...")
        client = mqtt.Client(mqtt_client_name)
        client.on_connect = on_connect 
        client.username_pw_set(mqtt_username, mqtt_password)
        client.connect(mqtt_host, mqtt_port, 60)
    except ConnectionRefusedError:
        print("Connection with MQTT-Server refused. Check MQTT connection settings!")
        print("Exiting...")
        exit(1)


