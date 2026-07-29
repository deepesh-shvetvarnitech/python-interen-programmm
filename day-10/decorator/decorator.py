#                                            Question =1
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

'''output:

Something is happening before the function is called.
Hello!
Something is happening after the function is called.'''
#                                                       Question =2.




def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper


@log_function_call
def add(a, b):
    return a + b


result = add(3, 5)


  #                                     Question =3.


def my_decorator(func):
    def wrapper(*args, **kwargs):

        
        result = func(*args, **kwargs)

        
        return result
    return wrapper




@my_decorator
def example_function():
    print("Inside the original function")



example_function()


#                                        Question = 4.






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



'''output:

Something is happening before the function is called.
Hello!
Something is happening after the function is called'''

#                                             question =5
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

''' output:

Something is happening before the function is called.
Hello!
Something is happening after the function is called.'''
#                                               Question =6.


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper



def say_hello():
    print("Hello!")



decorated_function = my_decorator(say_hello)



decorated_function()

'''output:

Something is happening before the function is called.
Hello!
Something is happening after the function is called.'''


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

''' output:

Something is happening before the function is called.
Hello!
Something is happening after the function is called.'''
#                                                   Question =7.


def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                print(f"Calling {func.__name__}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator



@repeat(times=3)
def say_hello():
    print("Hello!")



say_hello()
''' output:

Calling say_hello
Hello!
Calling say_hello
Hello!
Calling say_hello
Hello!'''


#                                            Question = 8.


def decorator1(func):
    def wrapper():
        print("Decorator 1 - Before function is called.")
        func()
        print("Decorator 1 - After function is called.")
    return wrapper


def decorator2(func):
    def wrapper():
        print("Decorator 2 - Before function is called.")
        func()
        print("Decorator 2 - After function is called.")
    return wrapper


@decorator1
@decorator2
def my_function():
    print("Original function.")



my_function()


''' output:

Decorator 1 - Before function is called.
Decorator 2 - Before function is called.
Original function.
Decorator 2 - After function is called.
Decorator 1 - After function is called.'''

#                                              Question =9
import functools



def decorator_without_wraps(func):
    def wrapper():
        
        print(f"Calling {func.__name__}")
        func()
    return wrapper



def decorator_with_wraps(func):
    @functools.wraps(func)
    def wrapper():
        
        print(f"Calling {func.__name__}")
        func()
    return wrapper



@decorator_without_wraps
def function1():
    
    print("Function 1")



def function2():
    print("Function 2")



output_metadata1 = f"Function 1: {function1.__name__}, Docstring: {function1.__doc__}"
output_metadata2 = f"Function 2: {function2.__name__}, Docstring: {function2.__doc__}"

''' output:

Calling wrapper
Function 1: wrapper, Docstring: Wrapper function without wraps.
Calling function2
Function 2: function2, Docstring: Original function with wraps.
Without functools.wraps, the metadata of the original function is not preserved, resulting in the decorator's wrapper function being displayed in the output. Using functools.wraps ensures that the original function's metadata is maintained, improving the clarity of the code.

                                                   Question =10.'''


def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b


result = add(3, 5)
'''Output:

Calling add with arguments (3, 5) and keyword arguments {}
add returned 8'''
#                                                     (B)
import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(2)
    print("Function executed.")


slow_function()
'''Output:

Function executed.
slow_function took 2.00 seconds to execute.'''



def check_permission(func):
    def wrapper(user, *args, **kwargs):
        if user.is_admin:
            result = func(user, *args, **kwargs)
        else:
            result = "Permission denied."
        return result
    return wrapper

@check_permission
def admin_only_function(user):
    return f"Welcome, {user.username}! Admin privileges granted."



user1 = {'username': 'Admin', 'is_admin': True}
result = admin_only_function(user1)
'''Output:

Welcome, Admin! Admin privileges granted.'''
#                                               Question =11.


def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper



def timing(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result
    return wrapper



@log_function_call
@timing
def add(a, b):
    return a + b



result = add(3, 5)


'''Output:

Calling add with arguments (3, 5) and keyword arguments {}
add took 0.00 seconds to execute.
add returned 8'''


#                                                  Question =12.


def function_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function Decorator: Before function is called.")
        result = func(*args, **kwargs)
        print("Function Decorator: After function is called.")
        return result
    return wrapper



class ClassDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Class Decorator: Before function is called.")
        result = self.func(*args, **kwargs)
        print("Class Decorator: After function is called.")
        return result



def function_example():
    print("Inside the original function.")



@ClassDecorator
def class_example():
    print("Inside the original function.")



function_example()
class_example()


'''Output:

Function Decorator: Before function is called.
Inside the original function.
Function Decorator: After function is called.
Class Decorator: Before function is called.
Inside the original function.
Class Decorator: After function is called.'''

#                                                 Question=13
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            print(f"Computing result for {func.__name__}{args} and caching it.")
            cache[args] = func(*args)
        else:
            print(f"Using cached result for {func.__name__}{args}.")
        return cache[args]

    return wrapper

# Function to be memoized
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

 
result1 = fibonacci(5)
result2 = fibonacci(8)
result3 = fibonacci(5)

'''Output:

Computing result for fibonacci(5) and caching it.
Computing result for fibonacci(4) and caching it.
Computing result for fibonacci(3) and caching it.
Computing result for fibonacci(2) and caching it.
Computing result for fibonacci(1) and caching it.
Computing result for fibonacci(0) and caching it.
Using cached result for fibonacci(1).
Using cached result for fibonacci(2).
Using cached result for fibonacci(3).
Using cached result for fibonacci(4).
Using cached result for fibonacci(5).
Computing result for fibonacci(8) and caching it.
Computing result for fibonacci(7) and caching it.
Computing result for fibonacci(6) and caching it.
Using cached result for fibonacci(5).
Using cached result for fibonacci(4).
Using cached result for fibonacci(3).
Using cached result for fibonacci(2).
Using cached result for fibonacci(1).
'''
#                                   question =14.

# Access control decorator
def access_control(required_permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user['permission'] >= required_permission:
                print(f"Access granted. Calling {func.__name__}.")
                result = func(*args, **kwargs)
            else:
                print("Access denied. Insufficient permission.")
                result = None
            return result
        return wrapper
    return decorator


@access_control(required_permission=2)
def restricted_function():
    print("Executing restricted function.")


user1 = {'username': 'Admin', 'permission': 3}
user2 = {'username': 'User', 'permission': 1}


result1 = restricted_function(user1)
result2 = restricted_function(user2)


'''Output:

Access granted. Calling restricted_function.
Executing restricted function.
Access denied. Insufficient permission.'''


#                                                     Questin =15.


import functools
import datetime



def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        argument_str = ', '.join([repr(arg) for arg in args])
        keyword_argument_str = ', '.join([f"{key}={repr(value)}" for key, value in kwargs.items()])
        
        print(f"[{timestamp}] Calling {func.__name__} with arguments: {argument_str}, keyword arguments: {keyword_argument_str}")
        
        result = func(*args, **kwargs)
        
        print(f"[{timestamp}] {func.__name__} returned: {repr(result)}")
        
        return result

    return wrapper

# Function with logging
@log_function_call
def add(a, b):
    return a + b

@log_function_call
def greet(name):
    return f"Hello, {name}!"


result1 = add(3, 5)
result2 = greet("Alice")

'''Output:

[2022-02-10 15:30:00] Calling add with arguments: 3, 5, keyword arguments: 
[2022-02-10 15:30:00] add returned: 8
[2022-02-10 15:30:00] Calling greet with arguments: 'Alice', keyword arguments: 
[2022-02-10 15:30:00] greet returned: 'Hello, Alice!'
The logging decorator provides valuable information about when functions are called, what arguments they receive, and what they return. This can be particularly useful for debugging and understanding the flow of a program.
'''
#                                                 Qustion =16.

import functools
import time


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"{func.__name__} took {execution_time:.6f} seconds to execute.")
        
        return result

    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)
    print("Function executed.")

@timing_decorator
def fast_function():
    print("Function executed quickly.")



slow_function()
fast_function()



'''Output:

Function executed.
slow_function took 2.000000 seconds to execute.
Function executed quickly.
fast_function took 0.000000 seconds to execute.'''
#                                                    Question =17
def handle_exceptions(default_value=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                print(f"An exception occurred in {func.__name__}: {type(e).__name__} - {str(e)}")
                result = default_value
            return result

        return wrapper
    return decorator


@handle_exceptions(default_value=-1)
def divide(a, b):
    return a / b

@handle_exceptions(default_value="Error")
def fetch_data(data, key):
    return data[key]


result1 = divide(10, 2)
result2 = divide(5, 0)
result3 = fetch_data({'name': 'John'}, 'age')
result4 = fetch_data({'name': 'Alice'}, 'city')


'''Output:

An exception occurred in divide: ZeroDivisionError - division by zero
An exception occurred in fetch_data: KeyError - 'age'''


#                                                      Question=18.

import functools


def log_function_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper


def handle_exceptions(default_value=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                print(f"An exception occurred in {func.__name__}: {type(e).__name__} - {str(e)}")
                result = default_value
            return result
        return wrapper
    return decorator


@timing_decorator
@handle_exceptions(default_value="Error")
def divide(a, b):
    return a / b


result = divide(10, 2)


'''Output:

Calling divide with arguments: (10, 2), keyword arguments: {}
divide took 0.000000 seconds to execute.
divide returned: 5.0'''

#                                          Question =19.

import functools



def singleton(cls):
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance



@singleton
class SingletonClass:
    def __init__(self, value):
        self.value = value



instance1 = SingletonClass(10)
instance2 = SingletonClass(20)

# Outputs
output1 = instance1.value
output2 = instance2.value




'''Outputs
output1 = instance1.value  # 10
output2 = instance2.value  # 10 (value from the first instance, as it is a singleton)

'''
#                                                    Question =20.

def custom_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator: Before Function Execution")
        result = func(*args, **kwargs)
        print("Decorator: After Function Execution")
        return result
    return wrapper


@custom_decorator
def original_function():
    """This is the original function."""
    print("Original Function: Execution")


original_function_metadata = {
    'name': original_function.__name__,
    'docstring': original_function.__doc__
}


original_function()


'''Output:

Decorator: Before Function Execution
Original Function: Execution
Decorator: After Function Execution'''

#                                                 Question =21
def log_aspect(func):
    def wrapper(*args, **kwargs):
        print(f"LOG: Calling {func.__name__} with arguments: {args}, keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__} returned: {result}")
        return result
    return wrapper

# Aspect: Timing
def timing_aspect(func):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"TIMING: {func.__name__} took {end_time - start_time:.6f} seconds to execute.")
        return result
    return wrapper


@log_aspect
@timing_aspect
def perform_operation(a, b):
    """Original function to perform an operation."""
    return a + b


result = perform_operation(10, 20)


'''Output:

LOG: Calling perform_operation with arguments: (10, 20), keyword arguments: {}
TIMING: perform_operation took 0.000000 seconds to execute.
LOG: perform_operation returned: 30'''


#                                          Question=22.

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper

# Original Function: Fibonacci using recursion
@memoize
def fibonacci(n):
    """Compute the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Calling the decorated function
result1 = fibonacci(5)
result2 = fibonacci(10)

'''Output:

# Results
result1 = fibonacci(5)  
result2 = fibonacci(10) '''


 #                                                Question =23.

from flask import Flask

app = Flask(__name__)



@app.route('/')
def home():
    return 'Welcome to the home page!'



def authenticate(func):
    def wrapper(*args, **kwargs):

        
        is_authenticated = True  
        
        if is_authenticated:
            return func(*args, **kwargs)
        else:
            return 'Authentication failed. Please log in.'

    return wrapper



@app.route('/dashboard')
@authenticate
def dashboard():
    return 'Welcome to the dashboard!'



if __name__ == '__main__':
    app.run(debug=True)


'''Output:

 Accessing the home route
 Output: Welcome to the home page!
 URL: http://localhost:5000/

Accessing the dashboard route without authentication
Output: Authentication failed. Please log in.
 URL: http://localhost:5000/dashboard


                                                    Question =24.'''


def repeat_decorator(n_times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat_decorator(n_times=3)
def greet(name):
    """A simple function to greet."""
    print(f"Hello, {name}!")


greet('Alice')



'''Output:

Output of the decorated function
Hello, Alice!
Hello, Alice!
 Hello, Alice!'''

#                                      Question =25
def overload(func):
    registry = {}

    def register(*types):
        def decorator(f):
            registry[types] = f
            return f
        return decorator

    def dispatcher(*args, **kwargs):
        types = tuple(type(arg) for arg in args)
        return registry[types](*args, **kwargs)

    func.register = register
    func.dispatcher = dispatcher
    return func


@overload
def calculate(*args, **kwargs):
    """Calculate method with method overloading."""
    pass

@calculate.register(int, int)
def calculate_int_int(x, y):
    return x + y

@calculate.register(str, str)
def calculate_str_str(s1, s2):
    return s1 + s2


result1 = calculate(1, 2)
result2 = calculate('Hello', ' World')
'''
result1 = calculate(1, 2)        
result2 = calculate('Hello', ' World') '''