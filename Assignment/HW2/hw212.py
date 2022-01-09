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
    def __init__(self, adapter, light):
        self.adapter = adapter
        self.light = light
        self.state = False

    def switchState(self, isOn: bool):
        self.state = isOn   # save the state        
        return self.light.switchState(isOn, self.adapter)
        

    # do not change function signature
    def setBrightness(self, lvl: Percent):
        if(self.state):
            self.light.setBrightness(lvl, self.adapter)    
        else:
            # Only adjust the brightness when the light was turned on. Else the bulb will light up in "off" state
            print("%s light was turned off. Ignore adjusting brightness" % (self.adapter.name)) 

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

    

# This abstract classes declare the interfaces to ensure the
# adaptees have the common function
class SmartLight:
    def switchState(self):
        raise NotImplementedError

    def setBrightness(self, isOn: bool, adapter):
        raise NotImplementedError

    def printOverheatWarning(self, adapter):
        print("%s light overheat! Abort switching on ..." % (adapter.name))


class LEDLight(SmartLight):
    def setBrightness(self, lvl, adapter):
        adapter.setPWM(lvl)

    def switchState(self, isOn: bool, adapter):
        if(isOn):
            if(adapter.temperature() <= CFG_LED_TEMPERATURE_MAX):
                adapter.setVoltage(CFG_LED_VOLTAGE)
            else: 
                self.printOverheatWarning(adapter)
                return -1
        else:
            adapter.setVoltage(0.0)

        



class BulbLight(SmartLight):
    def setBrightness(self, lvl, adapter):
        adapter.setVoltage(lvl * CFG_VOLTAGE_MAX // 100)

    def switchState(self, isOn: bool, adapter):
        if(isOn):
            if(adapter.temperature() <= CFG_BULB_TEMPERATURE_MAX):
                adapter.setVoltage(CFG_VOLTAGE_MAX)
            else: 
                self.printOverheatWarning(adapter)
        else:
            adapter.setVoltage(0.0)


# how we might test your code (examples)
# you can uncomment these for testing your solution but make sure 
# the following lines are commented before submitting.
# ----------------------------------------------------------
ledlight  = DimmLight(DimmAdapter('led'), LEDLight())
bulblight = DimmLight(DimmAdapter('bulb'), BulbLight())

g_esi['ledtemp'] = Kelvin(500)

print("Before Testing")
print(g_esi)

ledlight.switchState(False)
ledlight.switchState(True)
ledlight.setBrightness(80)


bulblight.switchState(True)
bulblight.setBrightness(80)
bulblight.switchState(False)
bulblight.setBrightness(25)
bulblight.switchState(True)
bulblight.setBrightness(20)

print("After Testing")
print(g_esi)