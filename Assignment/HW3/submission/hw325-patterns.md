1. The State Pattern
    The state pattern is needed to better manage and control the behaviour of the lights, groups or scenes. 
    In some scenario, the lights' logic depend on many rules (sensors' reliability, user input, etc.). If there are so many conditions to be considered, it is hard to debug and to find the causes when something wrong happens. Meanwhile, using states helps determine clearly which conditions and the results are related.   
        
    Assume that we have several additional sensors (motions, thermo, etc.) for the brightness control. The brightness adjustment only works if the ambient sensor is working and the the adjustment depends on the other sensors. If the controller has to check all sensor conditions to select the regulation method, the code is messy. Defining the desired logics in each states and substates is clearer. Moreoever, the behaviour is better designed and predicted (all transisitions are considered).


2. The Mediator Pattern
    Sometimes, there are some logical conflicts between multiple objects, the mediator pattern is helpful at a high level to manage these conflicts.  
    
    For example, we have two groups of light as "DiningLight" and "ReadingLight", both share several smart lights (the kitchen and the living room share some lights). Since "reading" require brighter light level, the DiningLight is not allowed to adjust the common lights. Without the mediator, the DiningLight group has to request the state of the ReadingLight group, which makes them coupled. 
    
    The mediator plays the role as a controller, which has its own rules or states. The mediator handles the conflicts by assigning priorities to each group and disable / overwrite the common lights according to the application.  

