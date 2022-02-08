"""
Rules Engine
"""

from typing import Callable, Any   # Typing Py3.x
import operator


class IntRel:
    """
    This class declares the integer operator
    """
    EQ = operator.eq
    LT = operator.lt
    GT = operator.gt

class BoolRel:
    """
    This class declares the boolean operator
    """
    NOT = operator.not_
    AND = operator.and_
    OR = operator.or_


class ICondition:
    def isTrue(self) -> bool:
        raise NotImplementedError 


class Action:
    def __init__(self, func : Callable, params = Any):
        self.method = func
        self.param = Any

    def exec(self):
        self.method(self.param)

class Rule:
    def __init__(self, name: str, condition: ICondition, action: Action):
        self.name = name
        self.cond = condition
        self.act = action

    def check(self):
        if self.cond.isTrue():
            self.act.exec()


class RulesEngine:
    def __init__(self):
        self.rule = dict()
    
    def addRule(self, r: Rule):
        self.rule[r.name] = r
        
    def delRule(self, name):
        del self.rule[name]

    def check(self):
        for key in self.rule:
            self.rule[key].check()


class BoolCondition(ICondition):
    def __init__(self, cond1: ICondition, rel: BoolRel, cond2: ICondition):
        self.cond1 = cond1
        self.rel = rel
        self.cond2 = cond2

    def isTrue(self):
        if self.rel is BoolRel.NOT:
            return self.rel(self.cond1.isTrue())
        else:
            return self.rel(self.cond1.isTrue(), self.cond2.isTrue())

class IntCondition(ICondition):
    def __init__(self, val: Callable, rel: IntRel, threshold: int):
        self.val = val
        self.thres = threshold
        self.rel = rel

    def isTrue(self):
        return self.rel(self.val(), self.thres)

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


