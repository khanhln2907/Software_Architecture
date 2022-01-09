import logging
import hw222 as smart_home

# The client code.
def main():

    ################################################################
    ########### 2.2.3 This is the beginning of your code ###########
    ################################################################

    # Create SmartHome
    
    # Initialize two observers: Alice and Bob

    # Attach observers to observable

    # Implement Storyline


    pass

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
    