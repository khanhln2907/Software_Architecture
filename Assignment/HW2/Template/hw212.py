"""
Smart ESI DimmAdapter with Composition
"""

## Imports [DO NOT CHANGE]
## =======================
from hw21x.units import *


## Constants [DO NOT CHANGE]
## =======================
CFG_LED_TEMPERATURE_MAX  = Kelvin(350)
CFG_BULB_TEMPERATURE_MAX = Kelvin(500)
CFG_VOLTAGE_MAX = Volt(230)
CFG_DUTY_MAX = Percent(100)


## Globals [DO NOT CHANGE]
## =======================
# we use this to read or inject values for your code
g_esi={
    'ledtemp': Kelvin(300),
    'ledduty': Percent(100),
    'ledvolt': Volt(0),
    'bulbtemp': Kelvin(300),
    'bulbduty': Percent(100),
    'bulbvolt': Volt(0)
}


## Classes
## =======================
class DimmLight():
    def __init__(self, adapter, light):
        self.adapter = adapter
        self.light = light
        self.state = False
        pass

    # do not change function signature
    def switchState(self, isOn: bool):
        self.state = isOn
        '''todo: overwrite or implement'''
        raise NotImplementedError 

    # do not change function signature
    def setBrightness(self, lvl: Percent):
        '''todo: overwrite or implement'''
        raise NotImplementedError 

    # you may add own functions here


class DimmAdapter():
    def __init__(self, name):
        self.name = name

    # set the Voltage level [DO NOT CHANGE]
    def setVoltage(self, voltage: Volt):
        g_esi[self.name+'volt'] = max(0, min(CFG_VOLTAGE_MAX, voltage))        
        print("{} set V={}".format(self.name, g_esi[self.name+'volt']))

    # set the PWM [DO NOT CHANGE]
    def setPWM(self, duty_cycle: Percent):
        g_esi[self.name+'duty'] = max(0, min(CFG_DUTY_MAX, duty_cycle))

    # get the temperature in Kelvin [DO NOT CHANGE]
    def temperature(self):
        return Kelvin(g_esi[self.name+'temp'])    




class LEDLight:
    pass # remove
    # todo: your code here


class BulbLight:
    pass # remove
    # todo: your code here





# how we might test your code (examples)
# you can uncomment these for testing your solution but make sure 
# the following lines are commented before submitting.
# ----------------------------------------------------------
ledlight  = DimmLight(DimmAdapter('led'), LEDLight())
ledlight.switchState(True)
ledlight.setBrightness(50)

bulblight = DimmLight(DimmAdapter('bulb'), BulbLight())
bulblight.switchState(True)
bulblight.setBrightness(50)

