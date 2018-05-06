import paho.mqtt.client as mqtt
THE_BROKER = "test.mosquitto.org"
THE_TOPIC = "CsoMAX60scalaEapt11-current"
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
	print("Connected to ", client._host, "port: ", client._port)
	print("Flags: ", flags, "return code: ", rc)
	client.subscribe(THE_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
td = client.connect(THE_BROKER, 1883, 60)
print(td)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
client.loop_forever()