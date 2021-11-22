"""
    In this example our button wants to connect to a light using sockets.
    For security reasons, the connect command only accepts an IP address in 
    a specific data format and not as string.

    Add your own code using the correct design pattern to make the connection work.

"""

class IPv4_Address():

    def __init__(self, byte1, byte2, byte3, byte4):
        self.bytes = (byte1, byte2, byte3, byte4)

    def __str__(self):
        return "{}.{}.{}.{}.".format(self.bytes[0], self.bytes[1], self.bytes[2], self.bytes[3])



class Socket():

    def connect( self, ip_addr ):
        if isinstance(ip_addr, IPv4_Address): # check the correct format
            print("Socket: connecting to {}".format( str(ip_addr) ))
        else:
            print("Socket: Invalid IP format!")


# main routine
def main():

    light_ip = "192.168.1.42"

    # connecting to light
    sock = Socket()
    sock.connect( light_ip )

    addr = IPv4_Address(192, 168, 1, 42)
    print( str(addr) )


#run
main()