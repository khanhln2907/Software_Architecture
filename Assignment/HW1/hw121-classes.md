
# Core Entities
**SwitchLight**: Every smart light has the common switching behaviour (on/off), this is handled by this class. Its brightness is constant

**DimmLight** This class is derived from the SwitchLight and additional method to adjust the brightness.

**MultiLight_Class**: abstract class, which group multiple lights together and is identified by an unique name. This class handles some common behaviours such as turning on/off the all lights in the group, changing color etc.

**Group**: is derived from *MultiLight_Class*, which defines its own method to set the same brightness for all lights belong to it.

**Scene**: is derived from *MultiLight_Class*, able to configure each individual lights with different brightness.

**Sensors**: abstract class, which samples the physical sensor and detects events triggered by users (from switches, software buttons, etc.). 

**DayLightSensor**: is derived from the class *Sensors*, which represents sensors sampling the intensity of the day lights (a Category of physical sensors)

**HardwareSwitch**: physical switches that trigger events.

**SoftwareButton**: software buttons defined by user to trigger events.

**Controller**: is assigned to a particular group or scene, update the sensor values and perform the desired control behaviours.

