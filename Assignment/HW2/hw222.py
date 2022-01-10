from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import logging
from hw22x.system_states import *

class Observable(ABC):
    """
    The Observable declares a set of methods for managing observers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass



class SmartHome(Observable):
    """
    The Publisher keeps track of (i) the current state
    """
    ################################################################
    ########### 2.2.2 This is the beginning of your code ###########
    ################################################################
    # Initialize state variable(s) _state
    _state = SmartHomeState.GARAGE_CLOSE_LIGHT_OFF
    _prev_state = SmartHomeState.UNDEFINED  
    _prev_prev_state = SmartHomeState.UNDEFINED 

    _light_state = False
    _garage_state = False

    ################################################################
    ########### 2.2.2 This is the end of your code #################
    ################################################################

    """
    For the sake of simplicity, the Observable's state, essential to all
    observers, is stored in this variable.
    """
    _observers: List[Observer] = []
    """
    List of observers. In real life, the list of observers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def attach(self, observer: Observer) -> None:
        self.logger.info("Observable: Attached an observer.")
        self._observers.append(observer)

    ################################################################
    ########### 2.2.3 This is the beginning of your code ###########
    ################################################################
    # Initiate one function: detach
    def detach(self, observer: Observer) -> None:
        return super().detach(observer)

    ################################################################
    ########### 2.2.3 This is the end of your code #################
    ################################################################

    """
    The subscription management methods.
    """
    def notify(self) -> None:
        """
        Trigger an update in each observer.
        """

        self.logger.info("Observable: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
            

    ################################################################
    ########### 2.2.2 This is the beginning of your code ###########
    ################################################################
    # Initiate four functions: turn_light_on, turn_light_off, open_garage, close_garage
    def turn_light_on(self):
        if(self._light_state is False):
            self.logger.info("SmartHome: Light turned On!")
            self._light_state = True
            new_state = SmartHomeState.map_state(garage_state = self._garage_state, light_state = True) 
            self.update_new_state(new_state)       

    def turn_light_off(self):
        if(self._light_state is True):
            self.logger.info("SmartHome: Light turned Off!")
            self._light_state = False
            self._prev_state = self._state
            new_state = SmartHomeState.map_state(garage_state = self._garage_state, light_state = False)
            self.update_new_state(new_state)       

    def open_garage(self):
        if(self._garage_state is False):
            self.logger.info("SmartHome: Garage opened!")
            self._garage_state = True
            new_state = SmartHomeState.map_state(garage_state = True, light_state = self._light_state)
            self.update_new_state(new_state)

    def close_garage(self):
        if(self._garage_state is True):
            self.logger.info("SmartHome: Garage closed!")
            self._garage_state = False
            new_state = SmartHomeState.map_state(garage_state = False, light_state = self._light_state)
            self.update_new_state(new_state)
            
    
    def update_new_state(self, new_state):
        self._prev_prev_state = self._prev_state
        self._prev_state = self._state
        self._state = new_state
        logging.info("%d --> %d --> %d", self._prev_prev_state, self._prev_state, self._state)
        self.notify()

    def get_states(self):
        return [self._state, self._prev_state, self._prev_prev_state]

    ################################################################
    ########### 2.2.2 This is the end of your code #################
    ################################################################
    

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Observable) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Observable they had been
attached to.
"""
################################################################
########### 2.2.2 This is the beginning of your code ###########
################################################################
# Initiate two classes: ObserverAlice, ObserverBob
class ObserverAlice(Observer):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        pass

    def update(self, subject: Observable) -> None:
        states = subject.get_states()
        if((states[2] is SmartHomeState.GARAGE_CLOSE_LIGHT_ON) and (states[1] is SmartHomeState.GARAGE_OPEN_LIGHT_ON) and (states[0] is SmartHomeState.GARAGE_CLOSE_LIGHT_ON)):
            self.logger.info("Notification: Hey Alice! You'll still have to turn off the light.")
        
        if((states[1] is SmartHomeState.GARAGE_OPEN_LIGHT_OFF) and (states[0] is SmartHomeState.GARAGE_OPEN_LIGHT_ON)):
            self.logger.info("Notification: Hey Alice! Bob forgot to close the garage")

class ObserverBob(Observer):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        pass

    def update(self, subject: Observable) -> None:
        states = subject.get_states()
        if((states[2] is SmartHomeState.GARAGE_CLOSE_LIGHT_ON) and (states[1] is SmartHomeState.GARAGE_OPEN_LIGHT_ON) and (states[0] is SmartHomeState.GARAGE_CLOSE_LIGHT_ON)):
            self.logger.info("Notification: Hey Bob! Alice forgot to turn off the light.")

        if((states[1] is SmartHomeState.GARAGE_OPEN_LIGHT_OFF) and (states[0] is SmartHomeState.GARAGE_OPEN_LIGHT_ON)):
            self.logger.info("Notification: Hey Bob! You'll still have to close the garage.")
################################################################
########### 2.2.2 This is the end of your code #################
################################################################



