"""
Exercise 1

Your Task:
    Write a simple python script(software) with the following requirements:
	    * The software should obtain inputs from a human agent
	    * The software should provide an output to a human agent
	    * On an input of three equal numbers, the software should output equilateral
	    * On an input of exactly two equal numbers, the software should output isosceles
	    * On an input where no number is equal to the other one, the software should output scalene.

Python Introduction:
 * python 10 minutes: https://www.stavros.io/tutorials/python/
 * interactive examples: https://www.learnpython.org/en/Classes_and_Objects
"""

'''
This function asks the user 3 input values and returns them in a list of strings
The list items have the same order as the input
For debugging, print line can be enabled
'''
def receive_inputs():
    input_a = input('Enter the first edge length a ==> ')
    input_b = input('Enter the second edge length b ==> ')
    input_c = input('Enter the third edge length c ==> ')
    print('a=', input_a, 'b=', input_b, 'c=', input_c)
    return [input_a,input_b,input_c]

'''
This function gets a list of three variables and compares them with each other
If exactly two of them are equal the return is isosceles
If all three are equal the return is equilateral
If non are equal to another, the return is scalene
'''
def select_triangle(edge_list):
    if(edge_list[0] == edge_list[1]):
        if(edge_list[1] == edge_list[2]):
            return "equilateral"
        else:
            return "isosceles"
    elif edge_list[1] == edge_list[2]:
        return "isosceles"
    elif edge_list[0] == edge_list[2]:
        return "isosceles"
    else:
        return "scalene"

'''
The main function simply runs the receive_inputs function
Then it uses these values as an input for the select_triangle function
The results of select_triangle function is displayed to the user
'''
def main():
    print("Waiting user to input edge values .....")
    edges=receive_inputs()
    triangle_type=select_triangle(edges)
    print(triangle_type)


main()