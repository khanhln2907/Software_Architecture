"""
    In the following, we want to support send() and receive() functions for 
    switches and lights INDEPENDENT from the underlying wireless protocol used.

    Use the bridge pattern to refactor the code. 
    Use python3 to test the code.

"""



# Defining the Wireless Protocols (DO NOT CHANGE THESE!)
# ======================================================
class WirelessSwitchable():

    def send(self, msg):
        # overwrite this
        raise NotImplementedError   

    def receive(self):
        # overwrite this
        raise NotImplementedError



class WiFi(WirelessSwitchable):
    packet = ""   # quick&diry – don't do this at home!

    def sendTCP(self, msg):
        print("WiFi: sending TCP packet: ", msg )
        WiFi.packet = msg

    def recvTCP(self):
        print("WiFi: received TCP packet: ", WiFi.packet )
        return WiFi.packet

    # overwrite and map
    def send(self, msg): self.sendTCP(msg)  
    def receive(self): return self.recvTCP()



class Bluetooth(WirelessSwitchable):
    packet = ""

    def request_service(self, srv):
        print("BT: requesting service: ", srv )
        Bluetooth.packet = srv

    def handle_service(self):
        print("BT: handeling service: ", Bluetooth.packet )
        return Bluetooth.packet

    # overwrite and map
    def send(self, msg): self.request_service(msg)
    def receive(self): return self.handle_service()



class ZigBee(WirelessSwitchable):
    packet = ""

    def sendIEEE(self, msg):
        print("ZigBee: sending IEEE 802.15.04 packet: ", msg )
        Bluetooth.packet = msg

    def recvIEEE(self):
        print("ZigBee: received IEEE 802.15.04 packet: ", Bluetooth.packet )
        return Bluetooth.packet

    # overwrite and map
    def send(self, msg): self.sendIEEE(msg)
    def receive(self): return self.recvIEEE()



# Base Classes (MAY BE CHANGED)
# ============================




class Switchable():
    def __init__(self):
        self._impl = None

    def set_protocol(self, protocol):
        self._impl = protocol

    def send(self, msg):
        self._impl.send(msg)

    def receive(self):
        return self._impl.receive()

    def on(self):
        raise NotImplementedError  

    def off(self):
        raise NotImplementedError  




# Derived Classes: Now only two general classes!
# ======================================================


class Switch(Switchable):
    def __init__(self, name):
        self.name = name
        super().__init__()  # requires python 3.x

    def on(self):
        print("{} Switch switched to ON!".format(self.name))
        self._impl.send("ON")

    def off(self):
        print("{} Switch switched to OFF!".format(self.name))
        self._impl.send("OFF")



class Light(Switchable):
    def __init__(self, name):
        self.name = name
        super().__init__()

    def on(self):
        print("{} Light switched ON!".format(self.name))

    def off(self):
        print("{} Light switched OFF!".format(self.name))

    def listen(self):
        packet = self._impl.receive()
        if packet == "ON":
            self.on()
        elif packet == "OFF":
            self.off()





# Main Function (CHANGED)
# ======================================================
def main():


    light = Light("Kitchen")
    switch = Switch("Kitchen")

    light.set_protocol( Bluetooth() )
    switch.set_protocol( Bluetooth() )  # change to WiFi to see effect

    switch.on()
    light.listen()


    time.sleep(2)
    print("Switching to ZigBee...")
    light.set_protocol( ZigBee() )
    switch.set_protocol( ZigBee() )
    time.sleep(3)


    switch.off()
    light.listen()



import time

#run
main()
