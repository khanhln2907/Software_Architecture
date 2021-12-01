# Explanation of Design Decisions

The system architecture was divided into 3 subsystems, which are SmartLights (individual lights, group, and scene), Sensors, and Controller.
# SmartLights Subsystem
**ConfigurableLight**

Group or scene (MultiLight_Base class) may contain both SwitchLight (SL) and DimmLight (DL). Treating them similarly might causes ambiguity. For instance, calling *configure()* to adjust the brightness but observe nothing at SwitchLights. Indeed, SL and DL should be decoupled such that only the configurable lights are adjusted. The class *ConfigurableLight* allow only lights' references in attribute *configHandle* of MultiLight_Base to be configured.

**MultiLight_Base**

This class treats common behaviours for a group of lights (for instance turn on/off all lights, which are frequent in real-world scenario) and allows further type of group to be implemented. The clients need only to define a desired settings, the activation and adjustment of lights are handled in this abstraction layer. (Encapsulation from external classes, such as controllers or sensors) 


# Sensor Subsystem
**SensorBase - Observer Model**

Sensor values and triggers are sampled by sensor instances. The results are notified to the subscriber. 

The *MainController* is interested in triggers to organize the sub-controllers.

The *ControllerBase* is interested in the sensor values for various purposes, e.g, continuous light intensity adjustment, energy saving, etc.

# Controller Subsystem
**ControllerBase - Adapter Model**

This class acts as an Observer, which provides sensor measurements to the groups. Furthermore, it let the child class define the control algorithm and this is activated by the MainController. The benefit of this is the encapsulation of groups, i.e, they can only be activated or deactivated, and their adjustment (brightness, state) are defined in the protected regulate() method.

**MainController**

The triggers from users are unpredictable and sometimes undesired. The main controller acts as a commander, which subscribe the triggers to activate / deactive sub-controllers reasonably. For instance, sub-controller with priorities, activity queues, or advanced strategies (e.g Memento)
