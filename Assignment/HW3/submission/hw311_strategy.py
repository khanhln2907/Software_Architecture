"""
Homework 311 with Strategy pattern
"""

class packet: # pylint: disable=too-few-public-methods
    """
    This class defines the packet data as interface between classes
    """
    def __init__(self, data):
        self.data = data


class PacketHandler:
    """
    This class contains the data packet and the assigned policy
    """
    def __init__(self, data_packet: packet):
        self.packet = data_packet
        self.policy = PacketStrategy()

    def setpolicy(self, policy):
        """
        This method sets the applied policy
        """
        self.policy = policy

    def process(self):
        """
        This method calls the setup policy to perform the data processing
        """
        self.policy.process(self.packet)

class PacketStrategy: # pylint: disable=too-few-public-methods
    """
    This abstract class declares the common interfaces
    for the child class with different strategies
    """
    def process(self, p: packet):
        """
        Child class must declare the strategy
        """
        raise NotImplementedError

class SSHHandler(PacketStrategy): # pylint: disable=too-few-public-methods
    """
    This class handles SSH packet
    """
    def process(self, p: packet):
        print("Processing SSH")
        print(p.data)

class TLSHandler(PacketStrategy): # pylint: disable=too-few-public-methods
    """
    This class handles TLS packet
    """
    def process(self, p: packet):
        print("Processing TLS")
        print(p.data)

class IPsecHandler(PacketStrategy): # pylint: disable=too-few-public-methods
    """
    This class handles IPSEC packet
    """
    def process(self, p: packet):
        print("Processing IPsec")
        print(p.data)

def main():
    """
    This function executes the test
    """
    # Create a specific packet
    my_packet = packet("[here is the packet data]")
    # Create the packet handler
    handler = PacketHandler(my_packet)
    # Set the policy to the handler
    my_policy = TLSHandler()
    handler.setpolicy(my_policy)
    # process the packet
    handler.process()


#main()
