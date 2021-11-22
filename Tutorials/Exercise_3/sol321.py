"""
    In this example a client wants to connect to a server.
    For security reasons, the connect command only accepts an IP address in 
    a specific data format and not as string.

    Add your own code using the correct design pattern to make the connection work.

"""

class IPv4_Address():

    def __init__(self, byte1, byte2, byte3, byte4):
        self.bytes = (byte1, byte2, byte3, byte4)

    def __str__(self):
        return "{}.{}.{}.{}".format(self.bytes[0], self.bytes[1], self.bytes[2], self.bytes[3])


class Socket():

    def connect( self, ip_addr ):
        if isinstance(ip_addr, IPv4_Address): # check the correct format
            print("Socket: connecting to {}".format( str(ip_addr) ))
        else:
            print("Socket: Invalid IP format!")


# Added code
# ===========================
class IPAdapter():

    def __init__(self, socket):
        self.socket = socket

    def connect( self, ip_addr ):
        try:
            a = ip_addr.split('.')
            ip_bytes = ( int(a[0]), int(a[1]), int(a[2]), int(a[3]) )
            if max(ip_bytes) > 255 or min(ip_bytes) < 0: raise ValueError
            ip_addr_struct = IPv4_Address(ip_bytes[0], ip_bytes[1], ip_bytes[2], ip_bytes[3] )
        except ValueError:
            print("Adapter: Invalid IP format!")
            return

        self.socket.connect(ip_addr_struct)
# ===========================


# main routine
def main():

    light_ip = "192.168.1.42"

    # connecting to light
    sock = Socket()

    ipadapter = IPAdapter( sock )
    ipadapter.connect( light_ip )


#run
main()