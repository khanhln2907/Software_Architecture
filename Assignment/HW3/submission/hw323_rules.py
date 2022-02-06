"""
Rules Engine
"""

from ast import Not, operator
from typing import Callable, Any   # Typing Py3.x
import operator
from smartl.trigger import Relation


class ICondition:
    def isTrue(self) -> bool:
        raise NotImplementedError 


class IntRel(Relation):
    """
    This class was already defined from IntRel
    """
    pass

class BoolRel():
    NOT = operator.not_
    AND = operator.and_
    OR = operator.or_

class IntCondition(ICondition):
    def __init__(self, threshold: int, rel: IntRel):
        self._threshold = threshold
        self._relation = rel

    def isTrue(self, inval: int):
        return eval(
            str(inval) + self._relation + str(self._threshold)
        )  # neither safe nor secure...


# example test code (same as in hw324)
def main():
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
    msg = Action(disable_powersaver, None)  # None is an optional parameter for Action.method
    rOfficeLight = Rule("Disabled Power-Saving", isWorkingHour, msg)

    re.addRule(rOfficeLight)


    for hour in range(0,24):
        g_theHour = hour
        print("\nh = {}: ".format(g_theHour), end='')
        re.check()


#main()


