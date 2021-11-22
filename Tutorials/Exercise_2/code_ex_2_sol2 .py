
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
This function checks the range and type of the number values and returns corresponding error values
If there is nothing wrong, the integer values are returned
If there is something wrong, value 0 is returned
'''
def check_inputs(edge_list):
    # Check whether each input is a number

    # Check a
    try:
        int_a = int(edge_list[0])
    except:
        print("User put a non number value for a")
        return 0
    # Check b
    try:
        int_b = int(edge_list[1])
    except:
        print("User put a non number value for b")
        return 0
    # Check c
    try:
        int_c = int(edge_list[2])
    except:
        print("User put a non number value for c")
        return 0
    # Checking for number finished
    
    # Check whether each number is greater than 0 
    if(int_a > 0 and int_b > 0 and int_c > 0):
        # All checks are valid, return 1
        return [int_a,int_b,int_c]
    else:
        print("All values must be greater than 0")
        return 0


'''
This function checks whether the values make a triangle. It does not include the equality case of triangle inequality
For every side this formula is used a < b + c
If there is nothing wrong, value 1 is returned
If there is something wrong, value 0 is returned
'''
def check_is_triangle(edge_list):

    # Get the edge values from the list
    a = edge_list[0]
    b = edge_list[1]
    c = edge_list[2]
    if(a < (b+c) and b < (a+c) and c < (b+a)):
        return 1
    else:
        print("Your values do not make a triangle in the first place")
        return 0

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
These values are checked to see if they are a number and greater than zero with check_inputs
Then they are checked whether they make a triangle
Then it uses these values as an input for the select_triangle function
Finally the results of select_triangle function is displayed to the user
'''
def main():
    print("Waiting user to input edge values .....")
    edges=receive_inputs()

    edges=check_inputs(edges)
    
    if (edges == 0):
        print("Your input values are not correct. Relaunch the software!")
    else:
        triangle_check = check_is_triangle(edges)
        if (triangle_check == 0):
            print("Your input values are not correct. Relaunch the software!")
        else:
            triangle_type = select_triangle(edges)
            print(triangle_type)

# Run the main function
main()
