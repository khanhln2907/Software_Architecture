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

"""
Following are class definitions for the 3 different types of triangles
The code is adapted from the previous exercise where instead of returning the triangle type,
the constructor assigns the edges
"""

class EquilateralTriangle():

    def __init__(self, edge_list):
        if(edge_list[0] == edge_list[1]):
            if(edge_list[1] == edge_list[2]):
                self.edges = edge_list
            else:
                raise Exception()
        else:
            raise Exception()

class IsoscelesTriangle():
    
    def __init__(self, edge_list):
        if(edge_list[0] == edge_list[1]):
            if(edge_list[1] == edge_list[2]):
                raise Exception()
            else:
                self.edges = edge_list
        elif edge_list[1] == edge_list[2]:
            self.edges = edge_list
        elif edge_list[0] == edge_list[2]:
            self.edges = edge_list
        else:
            raise Exception()

class ScaleneTriangle():

    def __init__(self, edge_list):
        if(edge_list[0] == edge_list[1]):
            if(edge_list[1] == edge_list[2]):
                raise Exception()
            else:
                raise Exception()
        elif edge_list[1] == edge_list[2]:
            raise Exception()
        elif edge_list[0] == edge_list[2]:
            raise Exception()
        else:
            self.edges = edge_list

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
The main function simply runs the receive_inputs function
Then it uses these values to instantiate different triangle classes
If the instantiation succeeds, the triangle type is printed
'''
def main():
    
    print("Waiting user to input edge values .....")
    edges=receive_inputs()
    
    try:
        equilateral_triangle = EquilateralTriangle(edges)
        print("Equilateral")
        return
    except:
        print("Trying other triangle types")
    
    try:
        isosceles_triangle = IsoscelesTriangle(edges)
        print("Isosceles")
        return
    except:
        print("Trying other triangle types")
        
    try:
        scalene_triangle = ScaleneTriangle(edges)
        print("Scalene")
        return
    except:
        print("Trying other triangle types")

main()