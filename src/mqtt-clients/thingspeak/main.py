#
# # File: example4.py
# #
# # A very simple example of an MQTT producer.
#
# import sys
# import time
# import random
# import sensor
#
# import paho.mqtt.client as mqtt
#
# THE_BROKER = "mqtt.thingspeak.com"
# THE_TOPIC_TMP = "channels/488582/publish/fields/field1/A82RXSUVX7BVO4D6"
# THE_TOPIC_HUM = "channels/488582/publish/fields/field2/A82RXSUVX7BVO4D6"
#
#
# mqttc=mqtt.Client()
# mqttc.connect(THE_BROKER, 1883, 60)
#
# mqttc.loop_start()
#
# while True:
#     data = sensor.read_tem_hum()
#     mqttc.publish(THE_TOPIC_TMP, data['tmp'])
#     time.sleep(5)
#     mqttc.publish(THE_TOPIC_TMP, data['hum'])
#     time.sleep(5)
#
#
# mqttc.loop_stop()

from mqtt import MQTTClient
import pycom
import sys
import time
import ufun
import json
import sensor

wifi_ssid = 'FabLab'
wifi_passwd = 'MakerFaire'
dev_id='70B3D549970B988C'

THE_BROKER = "mqtt.thingspeak.com"
THE_TOPIC_TMP = "channels/488582/publish/fields/field1/A82RXSUVX7BVO4D6"
THE_TOPIC_HUM = "channels/488582/publish/fields/field2/A82RXSUVX7BVO4D6"
THE_TOPIC = "channels/488582/publish/A82RXSUVX7BVO4D6"


def settimeout(duration):
   pass

def get_data_from_sensor(sensor_id="RAND"):
    # if sensor_id == "RAND":
    #     return ufun.random_in_range()
    return sensor.read_tem_hum();

### if __name__ == "__main__":

ufun.connect_to_wifi(wifi_ssid, wifi_passwd)

client = MQTTClient(dev_id, THE_BROKER, 1883)

print ("Connecting to broker: " + THE_BROKER)
try:
	client.connect()
except OSError:
	print ("Cannot connect to broker: " + THE_BROKER)
	sys.exit()
print ("Connected to broker: " + THE_BROKER)

print('Sending messages...')
while True:
    # creating the data
    the_data = get_data_from_sensor()
    # publishing the data
    # client.publish(THE_TOPIC_TMP, str(the_data['tmp']))
    # time.sleep(5)
    # client.publish(THE_TOPIC_HUM, str(the_data['hum']))
    client.publish(THE_TOPIC, 'field1={}&field2={}'.format(the_data['tmp'], the_data['hum']))
    time.sleep(5)
