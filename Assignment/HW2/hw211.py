"""
Smart ESI DimmAdapter with Inheritance
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

    # do not change function signature
    def switchState(self, isOn: bool):
        '''todo: overwrite or implement'''
        raise NotImplementedError 

    # do not change function signature
    def setBrightness(self, lvl: Percent):
        '''todo: overwrite or implement'''
        raise NotImplementedError 

    # you may add own functions here
    def __init__(self) -> None:
        self.brightness = 0
        self.state = False



class DimmAdapter(DimmLight):
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

    # some common functions for child classes
    def printTemperatureWarning(self):
        print("%s is too hot. Abort switching on!" %(self.name))

# Additional constants
CFG_LED_VOLTAGE = Volt(5)

class LEDLight(DimmAdapter):
    def __init__(self, name):
        self.name = name
        self.duty_cycle = 0

    # todo: your code here
    def switchState(self, isOn: bool):
        if(isOn):
            if(self.temperature() <= CFG_LED_TEMPERATURE_MAX):
                self.setVoltage(CFG_LED_VOLTAGE)
            else:
                self.printTemperatureWarning()
        else:
            self.setVoltage(0)

    def setBrightness(self, lvl: Percent):
        print("{} set duty_cycle={}%".format(self.name, lvl))
        self.setPWM(lvl)

class BulbLight(DimmAdapter):
    def __init__(self, name):
        self.name = name

    # todo: your code here
    def switchState(self, isOn: bool):
        if(isOn):
            if(self.temperature() <= CFG_BULB_TEMPERATURE_MAX):
                # Set the registered voltage for Bulb
                self.setVoltage(CFG_VOLTAGE_MAX)
            else:
                self.printTemperatureWarning()
        else:
            self.setVoltage(0)

    def setBrightness(self, lvl: Percent):
        voltage = Volt(230.0) * lvl // 100
        #print("{} adjusts brightness. Set V={}".format(self.name, voltage))
        self.setVoltage(voltage)
        

# how we might test your code (examples)
# you can uncomment these for testing your solution but make sure 
# the following lines are commented before submitting.
# ----------------------------------------------------------
ledlight = LEDLight('led')
ledlight.switchState(True)
ledlight.setBrightness(80)


bulblight = BulbLight('bulb')
bulblight.switchState(True)
bulblight.setBrightness(80)

# ledlight.switchState(False)
# bulblight.switchState(False)
# bulblight.switchState(True)




