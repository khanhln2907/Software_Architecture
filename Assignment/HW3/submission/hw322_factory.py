"""
Smart ESI LED
"""
from smartl.devices import *
from smartl.trigger import *
from smartl.lightcollections import *


class LightFactory:
    """
    This abstract class represents the factory pattern for Lights  
    """
    def __init__(self, lm):
        self._lm = lm 

    def createLight(self, name : str):
        light = self.createConcreteLight(name)
        self._lm.addLight(light)

    def createConcreteLight(self, name: str):
        raise NotImplementedError

class SwitchLightFactory(LightFactory):
    """
    This class declare the factory pattern for the SwitchLight class  
    """
    def createConcreteLight(self, name : str):
        return SwitchLight(name)

class DimmLightFactory(SwitchLightFactory):
    """
    This class declare the factory pattern for the DimmLight class  
    """
    def createConcreteLight(self, name : str):
        return DimmLight(name)


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


