from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import logging

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
        self.logger("Observable: Attached an observer.")
        self._observers.append(observer)

    ################################################################
    ########### 2.2.3 This is the beginning of your code ###########
    ################################################################
    # Initiate one function: detach

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

        self.logger("Observable: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
            

    ################################################################
    ########### 2.2.2 This is the beginning of your code ###########
    ################################################################
    # Initiate four functions: turn_light_on, turn_light_off, open_garage, close_garage


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


################################################################
########### 2.2.2 This is the end of your code #################
################################################################



