a = 4
b = 2
sum_r = a+b
diff_r= a-b
mul_r=a*b
div_r = a/b
rem_r=a%b
print("result of addition :",sum_r)
print("result of substraction :",diff_r)
print("result of multiplication:",mul_r)
print("result of divition :",div_r)
print("result of reminder :",rem_r)
is_equal=a==b
is_not_equal=a!=b
is_greater_then=a>b
is_greater_then=a>b
is_less_then=a<b
print("result of a=b is :",is_equal)
print("result of a!=b :",is_not_equal)
print("result of a>b :",is_greater_then)
print("result of a<b :",is_less_then)
print("result of reminder :",rem_r)
logical_and=(a>0)and(b>0)
logical_or=(a>0)or(b>0)
logical_not=not(b>0)
print("result of and is :",)
print("result of a!=b :",logical_and)
print("result of a>b :",logical_or)
print("result of a<b :",logical_and)
print("result of reminder :",rem_r)
                                    
number = 10
result = -number
print("Unary Minus Operator:", result)


result = +number
print("Unary Plus Operator:", result)


is_true = True
logical_not_result = not is_true
print("Logical NOT Operator:", logical_not_result)
                                    
a = 5
b = 3
addition_result = a + b
print("Binary Addition Operator:", addition_result)


multiplication_result = a * b
print("Binary Multiplication Operator:", multiplication_result)


bitwise_and_result = a & b
print("Bitwise AND Operator:", bitwise_and_result)
                                       
result = 5 + 3 * 2 / 2 - (4 % 3) ** 2

print("Result:", result)

                                        

a = 10
b = 3


addition_result = a + b


subtraction_result = a - b


multiplication_result = a * b


division_result = a / b


modulus_result = a % b


exponentiation_result = a ** b

print("Addition Result:", addition_result)
print("Subtraction Result:", subtraction_result)
print("Multiplication Result:", multiplication_result)
print("Division Result:", division_result)
print("Modulus Result:", modulus_result)
print("Exponentiation Result:", exponentiation_result)
                                
number = 15
divisor = 7


remainder = number % divisor

print(f"The remainder of {number} divided by {divisor} is: {remainder}")
                                           
list1 = [1, 2, 3]
list2 = [1, 2, 3]


result1 = list1 == list2


list3 = [1, 2, 3]
list4 = [1, 2, 3]


result2 = list3 is list4

print("Using == Operator:", result1)
print("Using is Operator:", result2)
                                    
num1 = 5
num2 = 10


result1 = (num1 > 0) and (num2 > 0)


num3 = -5
num4 = 10


result2 = (num3 > 0) or (num4 > 0)


flag = True


result3 = not flag

print("Using and Operator:", result1)
print("Using or Operator:", result2)
print("Using not Operator:", result3)
                                           

num1 = 5  
num2 = 3  

result_and = num1 & num2  


result_or = num1 | num2  

result_xor = num1 ^ num2  


result_left_shift = num1 << 1  
result_right_shift = num1 >> 1  

print("Bitwise AND:", result_and)
print("Bitwise OR:", result_or)
print("Bitwise XOR:", result_xor)
print("Left Shift:", result_left_shift)
print("Right Shift:", result_right_shift)
                                       

fruits = ['apple', 'banana', 'orange']


is_banana_in_list = 'banana' in fruits


is_grape_in_list = 'grape' in fruits


is_watermelon_not_in_list = 'watermelon' not in fruits


is_orange_not_in_list = 'orange' not in fruits

print("'banana' in fruits:", is_banana_in_list)
print("'grape' in fruits:", is_grape_in_list)
print("'watermelon' not in fruits:", is_watermelon_not_in_list)
print("'orange' not in fruits:", is_orange_not_in_list)

x = [1, 2, 3]
y = [1, 2, 3]
z = x


are_x_and_y_same = x is y


are_x_and_z_same = x is z


are_x_and_y_not_same = x is not y


are_x_and_z_not_same = x is not z

print("x is y:", are_x_and_y_same)
print("x is z:", are_x_and_z_same)
print("x is not y:", are_x_and_y_not_same)
print("x is not z:", are_x_and_z_not_same)

temperature = 25
weather = "Sunny" if temperature > 20 else "Cloudy"

print("Weather today:", weather)

x = 5
y = 10


result_lt = x < y


result_gt = x > y


result_lte = x <= y


result_gte = x >= y


result_ne = x != y


result_eq = x == y


print("x < y:", result_lt)
print("x > y:", result_gt)
print("x <= y:", result_lte)
print("x >= y:", result_gte)
print("x != y:", result_ne)
print("x == y:", result_eq)


x = 5


y = x
print("y (simple assignment):", y)


x += 3
print("x (after x += 3):", x)


x -= 2
print("x (after x -= 2):", x)


x *= 4

print("x (after x *= 4):", x)

x /= 2
print("x (after x /= 2):", x)


string_example = "Python"
char_to_check = "t"


is_present = char_to_check in string_example
print(f"Is '{char_to_check}' present in '{string_example}'? {is_present}")


list_example = [1, 2, 3, 4, 5]
element_to_check = 3


is_present = element_to_check in list_example
print(f"Is {element_to_check} present in {list_example}? {is_present}")

string_example = "PythonProgramming"


substring = string_example[6:16]  
print("Substring:", substring)


list_example = [1, 2, 3, 4, 5, 6, 7, 8, 9]


sublist = list_example[2:7]  
print("Sublist:", sublist)

base = 2
exponent = 3


result = base ** exponent
print("Result:", result)

dividend = 10
divisor = 3


result = dividend // divisor
print("Result:", result)

num1 = 5


num1 += 3
print("Result:", num1)


my_tupple = (1,2,3)
print("my tuple",my_tupple)
