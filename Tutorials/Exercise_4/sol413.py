"""
    Implement the observer pattern in the following code. 
    Remove the Controller class and implement the classes 
    Observerable and Observer. 
    
"""


ON = True
OFF = False




class Observable():
    def __init__(self):
        self.observers = []

    def attach( self, observer ):
        self.observers.append( observer )        

    def detach( self, observer ):
        self.observers.remove( observer ) 

    def notify( self, msg ):
        for observer in self.observers:
            observer.update( msg )


class Observer():
    def update(self, msg): raise NotImplementedError




class Switchable():
    def __init__(self, name):
        self.name = name
        self._state = OFF   # "_" means private member
        print("created ", name)

    def on(self):
        print("{} was switched ON!".format(self.name))
        self._state = ON

    def off(self):
        print("{} was switched OFF!".format(self.name))
        self._state = OFF

    def is_on(self):
        return self._state




class Light(Switchable, Observer):
    def __init__(self, name):
        Switchable.__init__(self, name+" Light")

    def update(self, msg):
        if msg == "ON": self.on()
        if msg == "OFF": self.off()



class Switch(Switchable, Observable):
    def __init__(self, name):
        Switchable.__init__(self, name+" Switch")
        Observable.__init__(self)
        #super().__init__(self)

    def on(self):
        super().on()
        self.notify("ON")

    def off(self):
        super().off()
        self.notify("OFF")










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

    # attach observer
    s1.attach( l1 )
    s2.attach( l1 ); s2.attach( l2 )
    s3.attach( l2 ); s3.attach( l3 )


    while True:
        states = receive_switch_toggles(3)

        for idx, switch in enumerate([s1, s2, s3]):
            if states[idx]:
                if switch.is_on():
                    switch.off()
                else:
                    switch.on()


#run
main()