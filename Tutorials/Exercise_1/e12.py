"""
Exercise 2

Your Task:
	Refactor the following file by using OOP features.

    Introduce classes for the controller, lights and buttons. 
    Every button should switch all lights when pressed.
    Make sure to output the names of the buttons and lights involved.
    Use at least 2 lights and 3 buttons.

    Test your program with 'python3 e12.py'

Python Introduction for OOP:
 * good examples: https://www.guru99.com/python-class-objects-object-oriented-programming-oop-s.html
 * interactive examples: https://www.learnpython.org/en/Classes_and_Objects
 * python 10 minutes: https://www.stavros.io/tutorials/python/
"""


def init():
    print("Connecting to WLAN... Success!")
    print("Controller boot finished.")


def kitchen_light_on():
    print("Kitchen light was switched ON!")


def kitchen_light_off():
    print("Kitchen light was switched OFF!")


def init_light_and_buttons():
    print("Initializing Light.")
    kitchen_light_off() # safe state
    print("Connecting to buttons... Success!")


# main routine
def main():
    print("Starting controller...")
    init() # controller
    init_light_and_buttons()
    light_state = OFF  # state of the light

    print("Entering main loop:")
    while True:
        (b1, b2) = receive_button_states(2) # 2 = number of buttons
        first_button_state = b1
        second_button_state = b2

        if first_button_state == PRESSED:
            print("Button next to door pressed.")
            if light_state == OFF:
                kitchen_light_on() # power light bulb
                light_state = ON
            else:
                kitchen_light_off()
                light_state = OFF               
 
        if second_button_state == PRESSED:
            print("Button next to window pressed.") 
            if light_state == OFF:
                kitchen_light_on()
                light_state = ON
            else:
                kitchen_light_off()
                light_state = OFF   




# Make any changes above. Do not edit below this line
# ===================================================================

# constant defines
PRESSED = True
RELEASED = False
ON = True
OFF = False

# output usage
def print_usage():
    print("In this example program, you can emulate button presses by entering the number of a button, or 'a' for pressing all buttons:\n\n\
    1: button_1 pressed\n\
    2: button_2 pressed\n\
    ...\n\
    a: all buttons pressed\n\
    else: no button pressed\n")    


# this function will emulate button press events which would be 
# received via socket communication from an IoT button.
def receive_button_states(num_buttons = 2):
    states = [False] * num_buttons
    choice = input("\nYour button press: ")
    try:
        idx = int(choice)-1
        if 0 <= idx <= num_buttons-1:
            states[idx] = True
    except ValueError:
        if choice == 'a': 
            states = [True] * num_buttons
    return states


# explain it
print_usage()

# run it
main()
