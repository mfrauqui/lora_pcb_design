from network import WLAN
import machine

wlan = WLAN(mode = WLAN.STATION)

def connect_to_wifi(ssid, auth):
    nets = wlan.scan()
    for net in nets:
        if(net.ssid == ssid):
             wlan.connect(net.ssid, auth=(WLAN.WPA2_ENT, config.username, config.password), identity=config.username, timeout=5000)
        while not wlan.isconnected():
            machine.idle()
        print("Succesfully connected with {}".format(net.ssid))
