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
    pass
    # todo: implement your code




# run your code
# given_rule()
test_new_rule()
