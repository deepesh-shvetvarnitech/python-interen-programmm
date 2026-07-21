#question = 1
def greet(name):

    print(f"helllo {name}")
greet("allice")    
'''
sol= hello alice
                                              question =1(b)'''
def add_numbers(a, b):
    
    result = a + b
    return result


sum_result = add_numbers(3, 7)
print("Sum:", sum_result)
'''
sol= sum:10
                                               question = 2'''
def greet(name):
    
    print(f"Hello, {name}!")

greet("alice")                              
'''
hello alice
                                                question = 3(same as previos)
                                                question =4'''
def square(number):
    
    return number ** 2


result = square(5)
print(f"The square of 5 is: {result}")
'''
the suare of 5: 25
                                                question=5'''
def add_numbers(x, y):
    sum_result = x + y
    return sum_result


result = add_numbers(3, 7)


print(f"The sum is: {result}")
'''
he sum is: 10
                                                 question = 6'''
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")


greet("Bob", "Good morning")
'''
Hello, Alice!
Good morning, Bob!
                                                question =7'''
def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


print_args(1, 2, 3, name="Alice", age=30)
print_args("Hello", "world", greeting="Hi")
'''
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 30}
Positional arguments: ('Hello', 'world')
Keyword arguments: {'greeting': 'Hi'}
                                                      question = 8'''
def example_function(arg1, *args, kwarg1="default_value", **kwargs):
    print("arg1:", arg1)
    print("Additional positional arguments (*args):", args)
    print("Keyword argument (kwarg1):", kwarg1)
    print("Additional keyword arguments (**kwargs):", kwargs)


example_function("value1", "value2", "value3", kwarg1="custom_value", key1="custom_key", key2="another_key")
'''
arg1: value1
Additional positional arguments (*args): ('value2', 'value3')
Keyword argument (kwarg1): custom_value
Additional keyword arguments (**kwargs): {'key1': 'custom_key', 'key2': 'another_key'}
                                                    question = 9'''
global_variable = "I am a global variable"

def example_function():
    
    local_variable = "I am a local variable"
    print(local_variable)

    
    print(global_variable)


example_function()
'''
I am a local variable
I am a global variable
                                                   question =10'''
def add(x, y):
    return x + y


add_lambda = lambda x, y: x + y


result_regular = add(3, 5)
result_lambda = add_lambda(3, 5)

print(f"Result (Regular Function): {result_regular}")
print(f"Result (Lambda Function): {result_lambda}")
'''
Result (Regular Function): 8
Result (Lambda Function): 8
                                                question = 11'''
def multiply(x, y):
    result = x * y
    return result



product = multiply(5, 3)
print(f"The product is: {product}")
'''
the  product is : 15 
                                                      question =12'''
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        
        return n * factorial(n - 1)


result = factorial(5)

print(f"The factorial of 5 is: {result}")
'''
The factorial of 5 is: 120
                                                        question =13'''
global_var = 10

def modify_global():
    
    
    
    global global_var
    
    print("Global variable inside function:", global_var)
    global_var += 5


modify_global()


print("Modified global variable outside function:", global_var)
'''
Global variable inside function: 10
Modified global variable outside function: 15
                                                Question =14
'''
def calculate_area(length, width):
    
                                             
    area = length * width
    return area

print(calculate_area.__doc__)


rectangle_area = calculate_area(5, 8)
print("Area of the rectangle:", rectangle_area)
'''
Output:

Calculate the area of a rectangle.

    Parameters:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.

Area of the rectangle: 40
                                                   Question =15'''
def placeholder_function():
    pass


placeholder_function()
'''
                                                    Question =16'''   
def outer_function(x):
    
    def inner_function(y):
        return x + y
    
    return inner_function


closure_1 = outer_function(10)
closure_2 = outer_function(5)


result_1 = closure_1(3)
result_2 = closure_2(3)


print(result_1)  
print(result_2)  
'''
13,8
                                                 Question =17'''    
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))


print("Squared numbers:", squared)  
print("Even numbers:", even_numbers)     
'''
     [1, 4, 9, 16, 25]
     [2, 4]

     Question =18'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()  
'''
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
                                                Question =18(b)'''
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Repeating {n} times:")
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Alice")



'''

Repeating 3 times:
Hello, Alice!
Hello, Alice!
Hello, Alice!
                                                Question =19'''
def greet(name):
    return f"Hello, {name}!"


result = greet("Alice")
print(result)
'''
hello,allice
                                              Quesstion=19(b)'''
class Greeter:
    def greet(self, name):
        return f"Hello, {name}!"


greeter_instance = Greeter()


result = greeter_instance.greet("Bob")
print(result)
'''
Hello, Bob!
                                              Question =20'''
def divide_numbers(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid data types"


result1 = divide_numbers(10, 2)
result2 = divide_numbers(5, 0)
result3 = divide_numbers("abc", 2)


print(result1)
print(result2)
print(result3)
'''
5.0
Error: Cannot divide by zero
Error: Invalid data types'''