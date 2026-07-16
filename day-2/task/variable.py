'''practice question of python 

                                     1
first_number = 5
second_number = 7
sum_result = first_number + second_number
print("Result = ", sum_result)
 
 solution      result=12

                                   2
A_variable = 24
S_string = "deepesh"
print("my variable is =", A_variable)
print("my string is =", S_string)
 solution        my variable is = 24
                my string is = deepesh
 
                                    3
Llist = [24,34,56,78]
list_id = (Llist)
print("my list id was ", list_id)
# soltion              my list id was  [24, 34, 56, 78]

#                                        4
def my_function():
    local_variable = 10
    print("Inside function:", local_variable)
my_function() solution     inside funtion: 10

                                     5
global_variable = 20
def my_function():
    print("Inside function:", global_variable)
my_function()
print("Outside function:", global_variable)
 # soltion outside funtion:20
   
                                     6
global_variable = 4 
def ex_function():
   local_variable = 5
   global_variable_inside_function = global_variable + 2
   print("Local variable inside function:", local_variable)
   print("Modified global variable inside function:", global_variable_inside_function)   
ex_function()
 
#soltion  Local variable inside function: 5
#Modified global variable inside function: 6 
                                      7
Iinteger= 24
Ffloat =24.3
Sstring ="deepesh"
is_true= True
Llist =[12,34,56,78]
Ttupple = (12,34,56,78)
Sset = {12,34,56}
Ddic = {'name':'deepsh', 'age':24}
print("integer",Iinteger)
print("Ffloat",Ffloat)
print("string",Sstring)
print("list",Llist)
print("tuple",Ttupple)
print("set",Sset)
print("dic",Ddic)
soltion integer 24
Ffloat 24.3
string deepesh
list [12, 34, 56, 78]
tuple (12, 34, 56, 78)
set {56, 34, 12}
dic {'name': 'deepsh', 'age': 24} 
                                    8
def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
x = 7
y = 3
x, y = swap_without_temp(x, y)

print("After swapping: x =", x, ", y =", y)
sol : After swapping: x = 3 , y = 7
                                 8
def swap_without_temp(a, b):
    a, b = b, a
    return a, b
x = 54
y = 103
x, y = swap_without_temp(x, y)

print("After swapping: x =", x, ", y =", y)
sol : After swapping: x = 103 , y = 54
                                  9

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("Using ==:")
print(a == b)
print(a == c)  
print("\nUsing is:")
print(a is b)  
print(a is c)  
sol: Using is:
False
True

                                10
x = 10
y = [1, 2, 3]

print("Before deletion:")
print("x =", x)
print("y =", y)

# Deleting variables
del x
del y[0]

print("\nAfter deletion:")

print("y =", y)
 sol : After deletion:
 y = [2, 3]

                                   11
variable = 10  
print("Variable is an integer:", variable)

variable = "Hello"  
print("Variable is a string:", variable)

variable = [1, 2, 3]  
print("Variable is a list:", variable)
Variable is an integer: 10
Variable is a string: Hello
Variable is a list: [1, 2, 3]
                                      12
first_name = "deepesh"
last_name = "chouhan"


full_name = first_name + " " + last_name
print("Full name using + operator:", full_name)


greeting = "Hello, "
name = "Alice"
greeting += name
print("Greeting using += shorthand:", greeting)
Full name using + operator: deepesh chouhan
Greeting using += shorthand: Hello, Alice
                                    13
original_list = [1, 2, 3]
print("Original list:", original_list)


original_list[0] = 44
print("Modified list:", original_list)
Original list: [1, 2, 3]
Modified list: [99, 2, 3]
                                    14
global_variable = 10

def modify_global_variable():
    global global_variable  
    global_variable = 20

modify_global_variable()

print("Modified global variable:", global_variable)
sol :Modified global variable: 20
                                     15
global_variable = 10

def example_function():
    local_variable = 20
    print("Local variables using locals():", locals())

example_function()variable_1 = 42
variable_2 = "Hello, Python!"
variable_3 = [1, 2, 3]

print("Type of variable_1:", type(variable_1))
print("Type of variable_2:", type(variable_2))
print("Type of variable_3:", type(variable_3))
print("\nGlobal variables using globals():", globals())
                                        16
variable_1 = 42
variable_2 = "Hello, Python!"
variable_3 = [1, 2, 3]

print("Type of variable_1:", type(variable_1))
print("Type of variable_2:", type(variable_2))
print("Type of variable_3:", type(variable_3))
                                 17
coordinates = (3, 7)


x, y = coordinates

print("Original tuple:", coordinates)
print("Unpacked variables - x:", x, ", y:", y)
 solution :Original tuple: (3, 7)
Unpacked variables - x: 3 , y: 7
            
variable_a = [1, 2, 3]  

variable_b = variable_a  

del variable_a  

print(variable_b)

variable_b = "Hello"
print(variable_b)
sol = [1, 2, 3]
Hello

nit = 12
flo = 12.4
string = "23"
float_from_integer = float(nit)
print("Float from integer:", float_from_integer)


integer_from_float = int(flo)
print("Integer from float:", integer_from_float)


integer_from_string = int(string)
print("Integer from string:", integer_from_string)

slotion : Float from integer: 12.0
Integer from float: 12
Integer from string: 23'''
import copy

original_list = [1, [2, 3], 4]

shallow_copied_list = copy.copy(original_list)


original_list[1][0] = 'X'

print("Original list:", original_list)  
print("Shallow copied list:", shallow_copied_list)  