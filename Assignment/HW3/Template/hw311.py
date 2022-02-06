class packet:
    def __init__(self, data):
        self.data = data


class PacketHandler:
        def __init__(self, packet):
            self.packet = packet

        def setpolicy(self, p):
            self.policy = p

        def processSSH(self):
            print("Processing SSH")
            print(self.packet.data)

        def processTLS(self):
            print("Processing TLS")
            print(self.packet.data)
               
        def processIPSEC(self):
            print("Processing IPSEC")
            print(self.packet.data)

        def process(self):
            if self.policy == "SSH":
                self.processSSH()
            if self.policy == "TLS":
                self.processTLS()
            if self.policy == "IPsec":
                self.processIPSEC()


def main():
    p = packet("[here is the packet data]")
    handler = PacketHandler(p)
    handler.policy= "TLS"
    handler.process()


main()
