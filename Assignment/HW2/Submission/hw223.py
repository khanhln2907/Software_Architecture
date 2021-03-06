import logging
import hw222 as smart_home

# The client code.
def main():

    ################################################################
    ########### 2.2.3 This is the beginning of your code ###########
    ################################################################

    # Create SmartHome
    home = smart_home.SmartHome()

    # Initialize two observers: Alice and Bob
    alice = smart_home.ObserverAlice()
    bob = smart_home.ObserverBob()

    # Attach observers to observable
    home.attach(alice)
    home.attach(bob)

    # Implement Storyline
    # Story 1
    home.open_garage()
    home.turn_light_on()
    home.close_garage()
    # Story 2
    home.open_garage()
    home.close_garage()
    # Story 3
    home.turn_light_off()
    home.open_garage()
    home.close_garage()
    # Story 4
    home.detach(alice)
    # Story 1 after detach
    logging.info("\n")
    logging.info("Stories without notification for Alice")
    home.open_garage()
    home.turn_light_on()
    home.close_garage()
    # Story 2 after detach
    home.open_garage()
    home.close_garage()

    ################################################################
    ########### 2.2.3 This is the end of your code #################
    ################################################################

def test():
    # Create SmartHome
    observable = smart_home.SmartHome()
    observable.open_garage()
    observable.turn_light_on()
    observable.close_garage()
    observable.turn_light_off()

if __name__ == "__main__":
    # Initialize logger - DO NOT CHANGE
    logger = logging.getLogger()
    file_handler = logging.FileHandler('hw223_test.log', mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    main()
    