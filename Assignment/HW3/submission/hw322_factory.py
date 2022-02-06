"""
Smart ESI LED
"""
from smartl.devices import *
from smartl.trigger import *
from smartl.lightcollections import *



class SwitchLightFactory:
    """
    This is the factory pattern of the switch light class
    """
    def __init__(self, lm):
        self.light_manager = lm 

    def createLight(self, name : str):
        new_light = SwitchLight(name)
        self.light_manager.addLight(new_light)


# example usage of your code
def main():

    # LightManager
    lm = LightManager()

    switch_lf = SwitchLightFactory(lm)

    # create light
    switch_lf.createLight("KitchenLight")

    # use lights
    lm.getLight("KitchenLight").switchOn()


# when submitting, leave it commented (no execution)
main()


