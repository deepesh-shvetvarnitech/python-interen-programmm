#                                           Question = 1
temp = 30
if temp > 30:
    print("its a hot day")
elif 30 > temp > 20:
    print("its moderate day")
else:
    print("its cold day")        
    #                                        solution
    #  its a cold day
    #                                      Question= 2
marks = -15
if marks>0:
    print("marks is positive")
elif marks<0:
    print("marks is negeative") 
else:
    print("marks is zero ")
 #                                        solution
 #                                           marks is negative
 #                                         Questin = 3
num=10
if num>0:
    print("num is positive") 
'''                                        soution
                                        num is positive
                                        Question = 4 '''
num = 10
if num>0:
    print("the num is positive")
    print("the num is inside the if block")
'''                                        solution
                                  the num is positive
                              the num is inside the if block'''
#                                        Question = 5
score = 75

if score >= 90:
    print("Excellent!")
elif 80 <= score < 90:
    print("Very Good.")
elif 70 <= score < 80:
    print("Good.")
elif 60 <= score < 70:
    print("Fair.")
else:
    print("Needs Improvement.")
'''                                  solution
                                     good 
                                     Question =6'''
score = 75

if score >= 60:
    print("Passing grade.")
    if score >= 90:
        print("Excellent!")
    elif score >= 80:
        print("Very Good.")
    elif score >= 70:
        print("Good.")
    else:
        print("Fair.")
else:
    print("Failing grade.") 
    '''
                                 soltion
                                passing grade
                                good.
                                 question = 7 '''
age = 20
message = "Teenager" if age >= 13 and age <= 19 else "Not a teenager"
print(message)  
'''                            solution
                              teenager
                                question = 8'''
x = 10

if x > 5:
    print("x is greater than 5")
else:
    pass 
'''
                                solution
                                x is greate then 5 
                                Question = 9'''
x = 5


assert x > 0, "Value of x should be greater than 0"

print("The value of x is:", x)  
'''                              solution
                                the value of x is : 5 
                                Question = 10'''
def say_hello():
    print("Hello from my_script!")


if __name__ == "__main__":
    say_hello()
    '''                              
                                    solution
                                    question= 11'''
Llist1 = [10,23,45,67,9]
Llist2 = [10,23,45,67,9]
print(Llist1==Llist2)
print(Llist1 is Llist2)
'''
                                   sol
                                   question= 12'''
age = 25
is_student = True


if age > 18 and is_student:
    print("You are an adult student.")
else:
    print("You are not an adult student.")


if age < 18 or is_student:
    print("You are either under 18 or a student.")
else:
    print("You are neither under 18 nor a student.")
'''
                                  sol

                                  question= 13'''
if 1:
    print("1 is truthy")

if "Hello":
    print("Hello is truthy")

if [1, 2, 3]:
    print("List is truthy")

# Falsy values
if 0:
    print("0 is falsy")
else:
    print("0 is falsy")

if "":
    print("Empty string is falsy")
else:
    print("Empty string is falsy")

if []:
    print("Empty list is falsy")
else:
    print("Empty list is falsy")
'''                             solution
                                1 is truthy
Hello is truthy
List is truthy
0 is falsy
Empty string is falsy
Empty list is falsy
                            Question=14'''
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    else:
        print(f"Result: {result}")
    finally:
        print("This block always executes")


divide_numbers(10, 2)
divide_numbers(5, 0)
'''
                            solution
                        Result: 5.0
This block always executes
Error: Division by zero is not allowed
This block always executes


                            Question= 15'''
fruits = ['apple', 'orange', 'banana']
if 'apple' in fruits:
    print("Apple is present in the list")
else:
    print("Apple is not present in the list")


colors = ('red', 'green', 'blue')
if 'yellow' not in colors:
    print("Yellow is not present in the tuple")
else:
    print("Yellow is present in the tuple")
'''
                                 sol
                                   Apple is present in the list
Yellow is not present in the tuple                     
                            Qustion =16'''
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping iteration for i =", i)
        continue  
    print("Inside the loop for i =", i)
    if i == 4:
        print("Breaking out of the loop for i =", i)
        break  
'''                         sol
                           Inside the loop for i = 1
Inside the loop for i = 2
Skipping iteration for i = 3
Inside the loop for i = 4
Breaking out of the loop for i = 4
                           Question = 17'''
def divide(a, b):
    assert b != 0, "Cannot divide by zero"  
    return a / b

# Test cases
result1 = divide(10, 2)
print("Result 1:", result1)

result2 = divide(8, 0)  
print("Result 2:", result2)
#                              Question = 18
def is_positive(x):
    return x > 0

def is_even(x):
    return x % 2 == 0


result_and = is_positive(5) and is_even(4)
print("Result (and):", result_and)


result_or = is_positive(-2) or is_even(6)
print("Result (or):", result_or) 
'''
                        solution 
                    Result (and): False
Result (or): True

                        Question = 19'''
def case1():
    return "This is case 1."

def case2():
    return "This is case 2."

def case3():
    return "This is case 3."

def default_case():
    return "This is the default case."

def switch_case(case_number):
    switch_dict = {
        1: case1,
        2: case2,
        3: case3
    }

    
    selected_case = switch_dict.get(case_number, default_case)
    return selected_case()


result1 = switch_case(1)
result2 = switch_case(2)
result3 = switch_case(3)
result_default = switch_case(5)

print(result1)
print(result2)
print(result3)
print(result_default)
'''
                                sol
                                This is case 1.
This is case 2.
This is case 3.
This is the default case.
                                question= 20'''
x = 10

if x > 5:
    result = "x is greater than 5"
else:
    result = "x is not greater than 5"

print(result)
'''
                              solution


                              '''