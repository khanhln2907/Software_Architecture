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

# Additional constants added by student
CFG_LED_VOLTAGE = Volt(5)


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
        self.state = isOn   # This variable ensures that the lights are not turned switchOn by adjusting the brightness
        if isOn:
            if self.isValidTemperature():
                self.switchOn()
            else:
                print("%s is too hot. Abort switching on!" %(self.getID()))
        else:
            self.switchOff()

    # do not change function signature
    def setBrightness(self, lvl: Percent):
        '''todo: overwrite or implement'''
        raise NotImplementedError

    # you may add own functions here
    def __init__(self):
        self.state = False

    # Any child class must define these functions to perform the behaviours of DimmLight
    # The adapter class should define only the hardware related methods

    def isValidTemperature(self):
        raise NotImplementedError

    def switchOn(self):
        raise NotImplementedError

    def switchOff(self):
        raise NotImplementedError

    # Child class defines the specific ID
    def getID(self):
        raise NotImplementedError
        

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

    def getID(self):
        return self.name

class LEDLight(DimmAdapter):
    def __init__(self, name):
        self.state = False
        self.name = name

    # todo: your code here
    def isValidTemperature(self):
        return self.temperature() <= CFG_LED_TEMPERATURE_MAX

    def switchOn(self):
        self.setVoltage(CFG_LED_VOLTAGE)
    
    def switchOff(self):
        return self.setVoltage(Volt(0))

    def setBrightness(self, lvl: Percent):
        # Only change the brightness if the light was switched on
        if self.state is True:
            print("{} sets duty_cycle={}%".format(self.name, lvl))
            self.setPWM(lvl)
        else:
            print("{} light was turned off. Ignore adjusting brightness.".format(self.name))

class BulbLight(DimmAdapter):
    def __init__(self, name):
        self.state = False
        self.name = name

    # todo: your code here
    def isValidTemperature(self):
        return self.temperature() <= CFG_BULB_TEMPERATURE_MAX

    def switchOn(self):
        self.setVoltage(CFG_VOLTAGE_MAX)

    def switchOff(self):
        return self.setVoltage(Volt(0))

    def setBrightness(self, lvl: Percent):
        # Only change the brightness if the light was switched on
        if self.state is True:
            print("{} adjusts brightness.".format(self.name))
            self.setVoltage(Volt(230.0) * lvl // 100)
        else:
            print("{} light was turned off. Ignore adjusting brightness.".format(self.name))


# how we might test your code (examples)
# you can uncomment these for testing your solution but make sure 
# the following lines are commented before submitting.
# ----------------------------------------------------------

# g_esi['ledtemp'] = Kelvin(200)

# print("Before Testing")
# print(g_esi)

# ledlight = LEDLight('led')
# ledlight.setBrightness(80)
# ledlight.switchState(False)
# ledlight.switchState(True)
# ledlight.setBrightness(80)


# bulblight = BulbLight('bulb')
# bulblight.switchState(True)
# bulblight.setBrightness(80)
# bulblight.switchState(False)
# bulblight.setBrightness(25)
# bulblight.switchState(True)
# bulblight.setBrightness(20)

# print("After Testing")
# print(g_esi)
