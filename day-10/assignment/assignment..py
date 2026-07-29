'''                                     SECTION =A
1(yield)
2) (Function returns a value but pauses)
3) (Parentheses ())
4) (An iterator that generates values lazily)
5) (Values one by one)
6) (Generator function)
7) ([0, 1, 2, 3, 4])
8)(Reading large log files line by line)
9) (Modify function behavior without changing its code)
10) (Apply a decorator to a function)
11) (Function decorator)
12)(Measure function execution time)
13)(Logs function calls before/after)
14)(Caching function results)
15) (Accept any arguments)
16) (Decorator factory)
17) (Generator expression)
18) (Next value)
19) (Stop a generator)
20) (API rate limiting, caching, logging, timing)

                                 SECTION =B
                                 QUESTION =1
                                 (A)
A generator is a special function that uses the yield keyword instead of return.

yield returns one value at a time.
After returning a value, the function pauses.
When called again, it continues from where it stopped.

                                (B)
def countdown_generator(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown_generator(5):
    print(num)
                               QUESTION = 2
                                  (A)
gen = (x**2 for x in range(10))                                                                                                 
                                   (B)
gen = (x**2 for x in range(5))

print(next(gen))
print(next(gen))
print(next(gen))
                          QUESTION =3
def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@decorator
def greet():
    print("Hello")

greet()
                               QUESTION = 4
                                 (A)
 def log_function_call(func):

    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper
                               (B)
 def log_function_call(func):

    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper
                            (C)
 def log_function_call(func):

    def wrapper():
        print("Function started")
        func()
        print("Function finished")

    return wrapper

                                         QUESTION =5
def read_file():

    yield "Line 1"
    yield "Line 2"
    yield "Line 3"


def logger(func):

    def wrapper(line):
        print("Processing:", line)
        func(line)

    return wrapper


@logger
def process_line(line):
    print(line.upper())


for line in read_file():
    process_line(line)
                                   SECTION = C
                                   QUESTION = 1
 def countdown_generator(n):

    while n > 0:
        yield n
        n -= 1


for number in countdown_generator(5):
    print(number)
                                QUESTION = 2
def read_large_file(filename):

    with open(filename, "r") as file:

        for line in file:
            yield line


for line in read_large_file("my_large_file.txt"):
    print(line.strip())
                                 QUESTION =3
data = [1,2,3,4,5,6,7,8,9,10]

even_squares = (x ** 2 for x in data if x % 2 == 0)

for number in even_squares:
    print(number)
                                   QUESTION =4
def log_function_call(func):

    def wrapper():

        print(f"--- Calling function: {func.__name__} ---")

        func()

        print(f"--- Function {func.__name__} finished ---")

    return wrapper


@log_function_call
def say_hello():
    print("Hello, Python!")


say_hello()
                                    QUESTION =5
import time

def timing_decorator(func):

    def wrapper(*args, **kwargs):

        
    
        start = time.time()

        
        
        result = func(*args, **kwargs)

        
        
        end = time.time()

        
        
        print(f"Function {func.__name__} took {end - start:.4f} seconds")

        return result

    return wrapper


@timing_decorator
def calculate_sum():

    time.sleep(2)      
    
    print("Calculation completed.")


calculate_sum()   

                                    QUESTION = 6
def cache_decorator(func):

    cache = {}

    def wrapper(*args, **kwargs):

        
    
        key = (args, tuple(kwargs.items()))

        
        
        if key in cache:
            print("Using cached result")
            return cache[key]

       
            
        result = func(*args, **kwargs)
        cache[key] = result

        return result

    return wrapper


@cache_decorator
def compute(x):

    print("Calculating...")
    return x * x


print(compute(5))
print(compute(5))
print(compute(8))   

                                SECTION =(D)

                                QUESTION =1
total_lines = 0
error_count = 0
warning_count = 0



def read_log_file(filename):

    with open(filename, "r") as file:

        for line in file:
            yield line.strip()



def log_line_processor(func):

    def wrapper(line):

        global total_lines
        global error_count
        global warning_count

        print(f"Reading Line : {line}")

        total_lines += 1

        if "ERROR" in line:
            error_count += 1

        if "WARNING" in line:
            warning_count += 1

        return func(line)

    return wrapper



@log_line_processor
def process_line(line):

    print("Processed :", line)



for line in read_log_file("app.log"):
    process_line(line)



    
print("\n------ Summary ------")
print("Total Lines :", total_lines)
print("Errors      :", error_count)
print("Warnings    :", warning_count) 

                                              QUESTION =2
 import time


 
def log_function_call(func):

    def wrapper(*args, **kwargs):

        print(f"Calling {func.__name__}")

        return func(*args, **kwargs)

    return wrapper



    
def timing_decorator(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Execution Time : {end-start:.4f} seconds")

        return result

    return wrapper



    
def cache_decorator(func):

    cache = {}

    def wrapper(*args, **kwargs):

        key = (args, tuple(kwargs.items()))

        if key in cache:
            print("Using Cached Data")
            return cache[key]

        result = func(*args, **kwargs)

        cache[key] = result

        return result

    return wrapper



    
def rate_limit(max_calls, period):

    calls = []

    def decorator(func):

        def wrapper(*args, **kwargs):

            current = time.time()

            while calls and current - calls[0] > period:
                calls.pop(0)

            if len(calls) >= max_calls:
                print("Rate Limit Exceeded")
                return

            calls.append(current)

            return func(*args, **kwargs)

        return wrapper

    return decorator



    
@rate_limit(max_calls=5, period=60)
@cache_decorator
@timing_decorator
@log_function_call
def get_user_data(user_id):

    print(f"Fetching data for User {user_id}")

    time.sleep(2)

    return {"id": user_id, "name": "Rahul"}



    
print(get_user_data(101))
print()

print(get_user_data(101))
print()

print(get_user_data(102))
print()

print(get_user_data(103))
print()

print(get_user_data(104))
print()

print(get_user_data(105))
print()

print(get_user_data(106))                                             













































































































































































































































































































































































































































































































'''