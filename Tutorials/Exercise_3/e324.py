
# Base Classes
# ============

class Switchable():

    def on(self):
        raise NotImplementedError  

    def off(self):
        raise NotImplementedError  




# Derived Classes for all combinations (REMOVE)
# =============================================


class WiFiSwitch(Switchable):
    def __init__(self, name):
        self.name = name
        self._wifi = WiFi()

    def on(self):
        print("{} Switch switched to ON!".format(self.name))
        self._wifi.sendTCP("ON")

    def off(self):
        print("{} Switch switched to OFF!".format(self.name))
        self._wifi.sendTCP("OFF")



class WiFiLight(Switchable):
    def __init__(self, name):
        self.name = name
        self._wifi = WiFi()

    def on(self):
        print("{} Light switched ON!".format(self.name))

    def off(self):
        print("{} Light switched OFF!".format(self.name))

    def listen(self):
        packet = self._wifi.recvTCP()
        if packet == "ON":
            self.on()
        elif packet == "OFF":
            self.off()


class BluetoothSwitch(Switchable):
    pass

class BluetoothLight(Switchable):
    pass


class ZigbeeSwitch(Switchable):
    pass

class ZigbeeLight(Switchable):
    pass




# Main Function (CHANGE)
# ======================================================
def main():


    light = WiFiLight("Kitchen")
    switch = WiFiSwitch("Kitchen")

    switch.on()
    light.listen()
    time.sleep(3)
    switch.off()
    light.listen()



import time

#run
main()
