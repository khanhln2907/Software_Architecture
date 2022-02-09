""" Rule Engine Example
Your task is to implement another example, similar to the following.
"""

from hw323_rules import RulesEngine, IntCondition, BoolCondition, IntRel, BoolRel, Rule, Action

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
    isAutoMode = True
    def checkAutoMode():
        return isAutoMode
    
    isSensorAvailable = True
    def checkSensor():
        return isSensorAvailable

    isTodayWorkingDay = False
    def checkWorkingDay():
        return isTodayWorkingDay

    def regulateBrightness(x = None):
        print(" Adjusting brightness ...", end='')
    
    def showAnimation(sec : int):
        print(" Showing animation for {} seconds on holiday!".format(sec), end = '')

    # Rules engine
    engine = RulesEngine()
      
    # Rule for showing the animation for 20 seconds on holidays
    isNormalDay = IntCondition(checkWorkingDay, IntRel.EQ, True) # check if today is the normal working day
    isChangeColor = BoolCondition(isNormalDay, BoolRel.NOT, None) # condition to be a holiday
    rChangeColor = Rule("Animation", isChangeColor, Action(showAnimation, 20)) # show animation for 20 seconds on holiday
    engine.addRule(rChangeColor)
    
    # Rule for using automatic brightness adjustment: 
    isSmartControlActivated = IntCondition(checkAutoMode, IntRel.EQ, True) # check if this mode is switched on
    isSensorWorking = IntCondition(checkSensor, IntRel.EQ, True) # check the sensors' availability
    isFeasible = BoolCondition(isSensorWorking, BoolRel.AND, isSmartControlActivated) # regulate only if sensors and mode are available
    rBrightnessAdjust = Rule("Brightness", isFeasible, Action(regulateBrightness, None))
    engine.addRule(rBrightnessAdjust)

    # Some testing variables 
    isAutoMode = False          # this simulates automatic mode is activated (True)
    isSensorAvailable = True    # this simulates sensors are available (True)
    isTodayWorkingDay = True    # this simulates holidays (False)

    # Test begins ...    
    for hour in range(0,24):
        print("\nTime = {} o'clock: \n".format(hour), end='')

        # Sensors and automatic control are turned off during midnight 
        if hour == 0:
            isAutoMode = False
            isSensorAvailable = False
        # In the morning, the sensors are activated
        elif hour == 6:
            isSensorAvailable = True
            print(" Ambient sensors start sampling...", end='\n')

        # At the midday, someone activates the brightness controller
        elif hour == 10:
            isAutoMode = True
            print(" Turned on automatic mode", end='\n')
        
        # Assume at 16 o'clock the sensors are defect
        elif hour == 16:
            isSensorAvailable = False
            print(" Ambient Sensors are defect", end='\n')

        elif hour == 18:
            isSensorAvailable = True
            print(" Ambient Sensors are available again", end='\n')

        elif hour == 20:
            print(" Automatic Mode is deactivated", end='\n')
            isAutoMode = False

        engine.check()


# run your code
#test_given_rule()
test_new_rule()
