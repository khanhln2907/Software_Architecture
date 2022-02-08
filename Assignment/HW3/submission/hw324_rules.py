""" Rule Engine Example
Your task is to implement another example, similar to the following.
"""

from scipy import rand
from hw323_rules import RulesEngine, IntCondition, BoolCondition, IntRel, BoolRel, Rule, Action
from smartl.devices import AmbientSensor, Clock

import random

def test_given_rule():
    g_theHour = 0

    def getHour():
        return g_theHour

    def disable_powersaver(x=None):
        print("Will not switch off after 10 minutes.", end='')


    # RuleEngine
    re = RulesEngine()

    # scenario: assume the lights have a power-save mode that will switch them off after 10min
    # create rule: During office hours, the lights should not be in power-save mode
    isAfter8 = IntCondition(getHour, IntRel.GT, 7)
    isBefore18 = IntCondition(getHour, IntRel.LT, 18)
    isWorkingHour= BoolCondition(isAfter8, BoolRel.AND, isBefore18)
    msg = Action(disable_powersaver, None)
    rOfficeLight = Rule("Disabled Power-Saving", isWorkingHour, msg)

    re.addRule(rOfficeLight)

    # illustrate rule by iterating over hours
    for hour in range(0,24):
        g_theHour = hour
        print("\nh = {}: ".format(g_theHour), end='')
        re.check()



def test_new_rule():
    # todo: implement your code

    isAutoMode = True
    def checkAutoMode():
        return isAutoMode
    
    isSensorAvailable = True
    def checkSensor():
        return isSensorAvailable

    def regulate_brightness(x = None):
        print("Adjusting brightness ...", end='')


    lightSensor = AmbientSensor("DarkerStimulator")
    
    # rules engine
    engine = RulesEngine()
      
    isSmartControlActivated = IntCondition(checkAutoMode, IntRel.EQ, True)
    isSensorWorking = IntCondition(checkSensor, IntRel.EQ, True)

    isFeasible = BoolCondition(isSensorWorking, BoolRel.AND, isSmartControlActivated)

    rBrightnessAdjust = Rule("Adjust Brightness", isFeasible, Action(regulate_brightness, None))

    engine.addRule(rBrightnessAdjust)

    # Some helping variables for the test
    timeSensorDefected = random.randint(11, 16)

    # Test begins ...    
    for hour in range(0,24):
        print("\n Time = {} o'clock: ".format(hour), end='')

        # Sensors and automatic control are turned off during midnight 
        if hour == 0:
            isAutoMode = False
            isSensorAvailable = False
        # In the morning, the sensors are activated
        elif hour == 6:
            print("Ambient sensors start sampling...", end='')
            isSensorAvailable = True

        # At the midday, someone activates the brightness controller
        elif hour == 10:
            print("Switched to automatic mode", end='')
            isAutoMode = True
        
        # Suddenly the sensor is unavailable for a while:
        elif hour == timeSensorDefected:
            print("Sensors are no longer available", end='')
            isSensorAvailable = False

        elif hour == 18:
            print("Good evening ...", end='')


        engine.check()
        #print("\n")

    #engine.check()






# run your code
# given_rule()
test_new_rule()
