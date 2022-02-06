"""
Smart ESI LED
"""
from smartl.devices import *
from smartl.trigger import *
from smartl.lightcollections import *



class SwitchLightFactory:
    pass # todo implement


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
# main()


