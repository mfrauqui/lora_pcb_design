# from mqtt import MQTTClient
# import time
# import sys
# import pycom
# import ufun
# import sensor
#
# wifi_ssid = 'FabLab'
# wifi_passwd = 'MakerFaire'
# dev_id = '70B3D549970B988C'
#
# broker_addr = 'iot.eclipse.org'
#
# def settimeout(duration):
#    pass
#
# def on_message(topic, msg):
#     print("Received msg: ", str(msg), "with topic: ", str(topic))
#
# ### if __name__ == "__main__":
#
# ufun.connect_to_wifi(wifi_ssid, wifi_passwd)
#
# client = MQTTClient(dev_id, broker_addr, 1883)
# client.set_callback(on_message)
#
# print ("Connecting to broker: " + broker_addr)
# try:
# 	client.connect()
# except OSError:
# 	print ("Cannot connect to broker: " + broker_addr)
# 	sys.exit()
# print ("Connected to broker: " + broker_addr)
#
# client.subscribe('tom2white/home/garden_R1/1029')
#
# print('Waiting messages...')
# while 1:
#     client.check_msg()
# # file: a_simple_pub.py

from mqtt import MQTTClient
import pycom
import sys
import time
import ufun
import json
import sensor

wifi_ssid = 'FabLab'
wifi_passwd = 'MakerFaire'
broker_addr = 'iot.eclipse.org'
dev_id = 'PMtest'

def settimeout(duration):
   pass

def get_data_from_sensor(sensor_id="RAND"):
    # if sensor_id == "RAND":
    #     return ufun.random_in_range()
    return sensor.read_tem_hum();

### if __name__ == "__main__":

ufun.connect_to_wifi(wifi_ssid, wifi_passwd)

client = MQTTClient(dev_id, broker_addr, 1883)

print ("Connecting to broker: " + broker_addr)
try:
	client.connect()
except OSError:
	print ("Cannot connect to broker: " + broker_addr)
	sys.exit()
print ("Connected to broker: " + broker_addr)

print('Sending messages...')
while True:
    # creating the data
    the_data = get_data_from_sensor()
    # publishing the data
    client.publish(dev_id+'/sdata', json.dumps(the_data))
    time.sleep(1)
