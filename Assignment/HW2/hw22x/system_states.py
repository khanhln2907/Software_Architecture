class SmartHomeState():
    UNDEFINED : int = -1
    GARAGE_CLOSE_LIGHT_OFF : int = 0
    GARAGE_OPEN_LIGHT_OFF : int = 1
    GARAGE_CLOSE_LIGHT_ON : int = 2
    GARAGE_OPEN_LIGHT_ON : int = 3

    @staticmethod
    def map_state(garage_state : bool, light_state : bool):
        if((garage_state is False) and (light_state is False)):
            return SmartHomeState.GARAGE_CLOSE_LIGHT_OFF
        elif((garage_state is False) and (light_state is True)):
            return SmartHomeState.GARAGE_CLOSE_LIGHT_ON
        elif((garage_state is True) and (light_state is False)):
            return SmartHomeState.GARAGE_OPEN_LIGHT_OFF
        else:
            return SmartHomeState.GARAGE_OPEN_LIGHT_ON


