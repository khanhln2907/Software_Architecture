# Devices – should contain classes such as SwitchLight and AmbientSensor
# You can and should add your own code but not delete any existing code.

import datetime
from hw231.config import *
from hw231.observer import *





class AmbientSensor():
    def __init__(self, name):
        self.lastValue = 100

    def measure(self): 
        # simulate 'getting darker'
        self.lastValue = max(self.lastValue-1, 0)

    def readVal(self):
        self.measure()
        print("{} measured {}".format(self.name, self.lastValue))
        return self.lastValue


class Clock(Sensor):
    def __init__(self, name):
        super().__init__(name)  

    def readVal(self):
        hour_now = datetime.datetime.now().hour
        print("{} measured {}".format(self.name, hour_now))
        return hour_now



class HwSwitch():
    def __init__(self, name):
        self._buttons = [False, False]
        
    def pressButton(self, idx: int):
        self._buttons[idx] = True
        print("{}.button[{}] was pressed.".format(self.name, idx))

    def _releaseButtons(self):
        self._buttons = [False, False]
        
    def readVal(self):
        return self._buttons[0] + self._buttons[1]*2



class SwitchLight():
    def __init__(self, name):
        self._state = False 

    def switchOn(self):
        self._state = True
        print("{} was switched ON!".format(self.name))

    def switchOff(self):
        self._state = False
        print("{} was switched OFF!".format(self.name))




class DimmLight():
    def __init__(self, name):
        self.brightness = 0 

    def setBrightness(self, lvl: Percent):
        self.brightness = lvl
        print("{} was dimmed to {}".format(self.name, self.brightness))
