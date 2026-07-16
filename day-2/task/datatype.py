''' opractice of datatypes
                                    1
tin = 24
flo = 24.4
string = "deepesh"
Llist = [24,24.3,"string"]
Sset = {1,2,3,4,5}
bol = True
Ttupple = (1,2,34,5,6,7,8,9)
dic = {'name':'deeps','age':24}
print("Integer:", tin)
print("Float:", flo)
print("String:", string)
print("Boolean:", bol)
print("List:", Llist)
print("Tuple:", Ttupple)
print("Set:", Sset)
print("Dictionary:", dict)
                                 soltion
  Integer: 24
Float: 24.4
String: deepesh
Boolean: True
List: [24, 24.3, 'string']
Tuple: (1, 2, 34, 5, 6, 7, 8, 9)
Set: {1, 2, 3, 4, 5}
Dictionary: <class 'dict'>
                                       2 

mutable_list = [1, 2, 3]


mutable_list[0] = 99

print("Mutable list:", mutable_list) 
                                    solution
        Mutable list: [99, 2, 3]  
                                    3 



tin = 42
print("Type of integer_variable:", type(tin))


flo = 3.14
print("Type of float_variable:", type(flo))


string = "Hello, Python!"
print("Type of string_variable:", type(string))


Llist = [1, 2, 3]
print("Type of list_variable:", type(Llist))


Ttuple = (10, 20, 30)
print("Type of tuple_variable:", type(Ttuple))
 
                                     solution
  Type of integer_variable: <class 'int'>
Type of float_variable: <class 'float'>
Type of string_variable: <class 'str'>
Type of list_variable: <class 'list'>
Type of tuple_variable: <class 'tuple'>    
                              4
tin = 24
print("integer value will be" , tin)
flo =23.2
print("float value will be", flo)
string ="deeepesh"
print("string will be",string)
com= 4+3J
print("complex number will be", com)
 solution will be:
integer value will be 24
float value will be 23.2
string will be deeepesh
complex number will be (4+3j)
                           5
string = "deepesh "
print("mu string will be",string)
Llist= [12,2.4,"string"]
print("my list will be",Llist)
tup= (12,34,56,5.6,"string")
print("my tupple will be", tup)
ran=range(5,10)
print("my range will be",ran)  
                             solution
     mu string will be deepesh 
my list will be [12, 2.4, 'string']
my tupple will be (12, 34, 56, 5.6, 'string')
my range will be range(5, 10)
                          6
lis=[12,23.4,"string"]
print("original list will be", lis)
tupp =(23,23.3,"string")
print("my tupple is :",tupp)
            solutiom
        riginal list will be [12, 23.4, 'string']
my tupple is : (23, 23.3, 'string')
                        7
sat = {1,2,34,56,31,78}
sat.add(24)
sat.remove(31)
print(sat)

set1 = {12,23,45,67,78}
set2 = {34,67,68,69,70}
uni = set1|set2
print(uni)
inter =  set1&set2                      
print(inter)
solution 
{1, 2, 34, 56, 24, 78}
{34, 67, 68, 69, 70, 12, 45, 78, 23}
{67}                    
                           8
string_variable = "Hello, Python!"


first_char = string_variable[0]
last_char = string_variable[-1]


substring = string_variable[7:13]


new_string = string_variable + " Welcome!"

print("Original string:", string_variable)
print("First character:", first_char)
print("Last character:", last_char)
print("Substring:", substring)
print("Concatenated string:", new_string)
                    solution
Original string: Hello, Python!
First character: H
Last character: !
Substring: Python
Concatenated string: Hello, Python! Welcome!
                                     9
is_python_fun = True
is_learning = False


result_and = is_python_fun and is_learning
result_or = is_python_fun or is_learning
result_not = not is_python_fun

print("Is Python fun?", is_python_fun)
print("Is learning?", is_learning)
print("Result of AND operation:", result_and)
print("Result of OR operation:", result_or)
print("Result of NOT operation:", result_not)
                                    solution
Is Python fun? True
Is learning? False
Result of AND operation: False
Result of OR operation: True
Result of NOT operation: False
                                       10
int_variable = 42
float_variable = float(int_variable)


float_number = 3.14
int_number = int(float_number)


number = 123
string_number = str(number)

print("Original integer:", int_variable)
print("Converted to float:", float_variable)

print("Original float:", float_number)
print("Converted to integer:", int_number)

print("Original integer:", number)
print("Converted to string:", string_number)
 solution
Original integer: 42
Converted to float: 42.0
Original float: 3.14
Converted to integer: 3
Original integer: 123
Converted to string: 123
                                    11
empty_dict1 = {}
print("Empty dictionary 1:", empty_dict1)


empty_dict2 = dict()
print("Empty dictionary 2:", empty_dict2)
                                solution
Empty dictionary 1: {}
Empty dictionary 2: {}
                                    12
import copy


original_dict = {'key': [1, 2, 3]}


shallow_copy_dict = copy.copy(original_dict)


shallow_copy_dict['key'][0] = 99

print("Original dictionary:", original_dict)
print("Shallow copy dictionary:", shallow_copy_dict)
                             solu
Original dictionary: {'key': [99, 2, 3]}
Shallow copy dictionary: {'key': [99, 2, 3]}
                                 13
original_string = "Python is amazing!"


substring = original_string[7:10]
print("Substring:", substring)


every_second = original_string[0::2]
print("Every second character:", every_second)

original_list = [1, 2, 3, 4, 5]


sublist = original_list[1:4]
print("Sublist:", sublist)

reversed_list = original_list[::-1]
print("Reversed list:", reversed_list)
                               solu
Substring: is 
Every second character: Pto saaig
Sublist: [2, 3, 4]
Reversed list: [5, 4, 3, 2, 1]
                               14

my_list = [1, 2, 3, 3, 4, 5]
print("List:", my_list)


my_set = {1, 2, 3, 3, 4, 5}
print("Set:", my_set)
                            solu
List: [1, 2, 3, 3, 4, 5]
Set: {1, 2, 3, 4, 5}   
                           15
def square_numbers(n):
    for i in range(n):
        yield i ** 2


for num in square_numbers(5):
    print("Generated:", num)
      solutiom
    Generated: 0
Generated: 1
Generated: 4
Generated: 9
Generated: 16
                          16
my_list = [1, 2, 3, 4, 5]
length_of_list = len(my_list)
print("Length of the list:", length_of_list)


my_string = "Python"
length_of_string = len(my_string)
print("Length of the string:", length_of_string)
                       solution
ength of the list: 5
Length of the string: 6
                             17
def simple_function():
    print("This function doesn't return anything.")


result = simple_function()


if result is None:
    print("The function returned None.")
else:
    print("The function returned a value.")
                             18
                             
my_bytes = b'Hello'
print("bytes:", my_bytes)


my_bytearray = bytearray(b'Python')
print("bytearray:", my_bytearray)


my_bytearray[0] = 80
print("Modified bytearray:", my_bytearray)
                     solution
This function doesn't return anything.
The function returned None.
bytes: b'Hello'
bytearray: bytearray(b'Python')
Modified bytearray: bytearray(b'Python')
                              19
my_frozenset = frozenset([1, 2, 3, 4, 5])
print("frozenset:", my_frozenset)


try:
    my_frozenset.add(6)
except AttributeError as e:
    print("Error:", e)
                     soltion

    frozenset: frozenset({1, 2, 3, 4, 5})
                        20
is_python_fun = True
is_java_fun = False

print("Is Python fun?", is_python_fun)
print("Is Java fun?", is_java_fun)

# None
result = None
if result is None:
    print("No result available.")
                 solution
    s Python fun? True
Is Java fun? False
No result available.'''
