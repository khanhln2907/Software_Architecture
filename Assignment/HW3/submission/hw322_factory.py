"""
Smart ESI LED
"""
from smartl.devices import *
from smartl.trigger import *
from smartl.lightcollections import *


class SwitchLightFactory:
    """
    This class represents the factory pattern for the SwitchLight class  
    """
    def __init__(self, lm):
        self._lm = lm 

    def createLight(self, name : str):
        new_light = SwitchLight(name)
        self._lm.addLight(new_light)

class DimmLightFactory(SwitchLightFactory):
    """
    This class represents the factory pattern for the DimmLight class  
    """
    def createLight(self, name : str):
        new_light = DimmLight(name)
        self._lm.addLight(new_light)


# example usage of your code
def main():

    # LightManager
    lm = LightManager()

    switch_lf = SwitchLightFactory(lm)  
    # create light
    switch_lf.createLight("KitchenLight")

    # use lights
    lm.getLight("KitchenLight").switchOn()


    # tests added by students
    dimm_lf = DimmLightFactory(lm) 
    dimm_lf.createLight("DimmLight")
    lm.getLight("DimmLight").switchOn()
    lm.getLight("DimmLight").setBrightness(20)

# when submitting, leave it commented (no execution)
#main()


