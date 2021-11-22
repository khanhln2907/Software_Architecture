"""
    Implement the observer pattern in the following code. 
    Remove the Controller class and implement the classes 
    Observerable and Observer. 
    
"""

import threading, time
ON = True
OFF = False





class Switchable():
    def __init__(self, name):
        self.name = name
        self._state = OFF   # "_" means private member
        self._switched = False
        print("created ", name)

    def on(self):
        print("{} was switched ON!".format(self.name))
        self._state = ON
        self._switched = True

    def off(self):
        print("{} was switched OFF!".format(self.name))
        self._state = OFF
        self._switched = True

    def was_switched(self):
        copy = self._switched
        self._switched = False
        return copy

    def is_on(self):
        return self._state




class Light(Switchable):
    def __init__(self, name):
        super().__init__(name+" Light")




class Switch(Switchable):
    def __init__(self, name):
        super().__init__(name+" Switch")





class Controller(threading.Thread):
    def __init__(self, switches):
        self.switches = []+switches # expert question: why []+ ?
        self.light_map = [ [] ]*len(switches)
        print("init controller")
        threading.Thread.__init__(self)


    def set_lights_for_switch(self, switch, lights):
        print("Setting lights for ", switch.name)
        idx = 0
        for idx, entry in enumerate(self.switches):
            if entry.name == switch.name: break

        # print(idx)
        self.light_map[ idx ] = lights


    def run(self):
        while True:
            for switch_idx, lights in enumerate(self.light_map):
                #print("running")
                if self.switches[switch_idx].was_switched():
                    for light in lights:
                        if light.is_on():
                            light.off()
                        else:
                            light.on()




# do not change this function
def receive_switch_toggles(num_buttons = 2):
    states = [False] * num_buttons
    choice = input("\nYour switch toggle: ")
    try:
        idx = int(choice)-1
        if 0 <= idx <= num_buttons-1:
            states[idx] = True
    except ValueError:
        if choice == 'a': 
            states = [True] * num_buttons
    return states


# main routine
def main():


    # create lights
    l1 = Light("Kitchen")
    l2 = Light("Living Room")
    l3 = Light("Bedroom")

    # create buttons
    s1 = Switch("Door")
    s2 = Switch("Window")
    s3 = Switch("Desk")


    ctrl = Controller( [s1] )

    ctrl.set_lights_for_switch( s1, [l1] )
    ctrl.set_lights_for_switch( s2, [l1, l2] )
    ctrl.set_lights_for_switch( s3, [l2, l3] )

    ctrl.start()  # start thread


    while True:
        states = receive_switch_toggles(3)

        for idx, switch in enumerate(ctrl.switches):
            if states[idx]:
                if switch.is_on():
                    switch.off()
                else:
                    switch.on()
            time.sleep(1)

#run
main()