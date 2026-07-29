#                                          GENERRATOR = 1
def generate_squares(n):
    for i in range(n):
        yield i ** 2


squares = list(generate_squares(5))

print(squares)
'''
[0, 1, 4, 9, 16]
                                             QUESTON=2 '''
def regular_function(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result



def generator_function(n):
    for i in range(n):
        yield i ** 2



regular_result = regular_function(5)


generator_result = list(generator_function(5))



print("Regular Function:", regular_result)
print("Generator Function:", generator_result)
'''
Regular Function: [0, 1, 4, 9, 16]
Generator Function: [0, 1, 4, 9, 16]
                                                (b)'''
large_list = regular_function(1000000)



large_generator = generator_function(1000000)



import sys
print("Memory Usage (Regular Function):", sys.getsizeof(large_list))
print("Memory Usage (Generator Function):", sys.getsizeof(large_generator))


#                                             QUESTION=3
def generate_squares(n):
    for i in range(n):
        yield i ** 2



squares = list(generate_squares(5))



print(squares)
'''The output :

[0, 1, 4, 9, 16]'''
#                                        QUESTION=4
def simple_generator():
    yield 1
    yield 2
    yield 3



gen = simple_generator()



print(next(gen))  
print(next(gen))  
print(next(gen))  


#                                        QUETION = 5
def generate_squares(n):
    for i in range(n):
        yield i ** 2



squares_generator = generate_squares(5)


value1 = next(squares_generator)
value2 = next(squares_generator)
value3 = next(squares_generator)

print("Lazy Evaluation Results:")
print("Value 1:", value1)
print("Value 2:", value2)
print("Value 3:", value3)
'''
Lazy Evaluation Results:
Value 1: 0
Value 2: 1
Value 3: 4
 

                                        QUESTION = 6'''
def generate_squares_list(n):
    return [i ** 2 for i in range(n)]



def generate_squares_generator(n):
    for i in range(n):
        yield i ** 2



squares_list = generate_squares_list(5)
squares_generator = generate_squares_generator(5)



print("Using List:")
print(squares_list)

print("\nUsing Generator:")
print(list(squares_generator))
'''Using List:
[0, 1, 4, 9, 16]

Using Generator:
[0, 1, 4, 9, 16]
'''

#                                              QUESTION=7

def generate_infinite_sequence():
    i = 0
    while True:
        yield i
        i += 1



infinite_generator = generate_infinite_sequence()



first_five_values = [next(infinite_generator) for _ in range(5)]

print("First Five Values from Infinite Generator:", first_five_values)
'''
First Five Values from Infinite Generator:
[0, 1, 2, 3, 4]

                                                 QUETION =8'''
def generate_sequence(limit):
    i = 0
    while i < limit:
        yield i
        i += 1


limited_generator = generate_sequence(3)



values = list(limited_generator)



try:
    next(limited_generator)
except StopIteration as e:
    exhausted_message = str(e)

print("Consumed Values:", values)
print("Exhausted Message:", exhausted_message)
'''
Consumed Values:
[0, 1, 2]
Exhausted Message: 



                                                    QUESTION = 9'''

def generate_sequence(limit):
    i = 0
    while i < limit:
        yield i
        i += 1



limited_generator = generate_sequence(3)



value1 = next(limited_generator)
value2 = next(limited_generator)
value3 = next(limited_generator)



try:
    value4 = next(limited_generator)
except StopIteration as e:
    exhausted_message = str(e)

print("Values using next():", value1, value2, value3)
print("Exhausted Message:", exhausted_message)
'''
Values using next():
0 1 2
Exhausted Message: 


                                               QUESTION =10'''
list_comprehension = [x ** 2 for x in range(5)]


 
generator_expression = (x ** 2 for x in range(5))



print("List Comprehension:", list_comprehension)
print("Generator Expression:", list(generator_expression))
'''
List Comprehension:
[0, 1, 4, 9, 16]

Generator Expression:
[0, 1, 4, 9, 16]

                                            QUETION =11'''
def generate_squares(n):
    for i in range(n):
        yield i ** 2



squares_generator = generate_squares(5)



print("Generator Function:")
print(list(squares_generator))
'''
Generator Function:
[0, 1, 4, 9, 16]

                                         QUESTION =11(b)'''
generator_expression = (i ** 2 for i in range(5))



print("Generator Expression:")
print(list(generator_expression))
'''
Generator Expression:
[0, 1, 4, 9, 16]
                                          QUESTION = 12'''
def generator_with_send():
    value = yield "First yield"
    yield f"Received value: {value}"



my_generator = generator_with_send()



first_yield_result = next(my_generator)




second_yield_result = my_generator.send("Hello, Generator!")

print(first_yield_result)
print(second_yield_result)
'''
First yield
Received value: Hello, Generator!'''

#                                       QUESTION=13
def generator_outer():
    yield "Start of Outer Generator"
    yield from generator_inner()
    yield "End of Outer Generator"

def generator_inner():
    yield "Start of Inner Generator"
    yield "Value from Inner Generator"
    yield "End of Inner Generator"



my_generator = generator_outer()



for value in my_generator:
    print(value)
    '''
    
Start of Outer Generator
Start of Inner Generator
Value from Inner Generator
End of Inner Generator
End of Outer Generator'''


#                                                   QUESTION =14.


def numbers_up_to(n):
    for i in range(1, n + 1):
        yield i

def square_numbers(iterable):
    for num in iterable:
        yield num ** 2

def filter_odd_numbers(iterable):
    for num in iterable:
        if num % 2 != 0:
            yield num



pipeline_result = filter_odd_numbers(square_numbers(numbers_up_to(5)))



print("Generator Pipeline Result:")
print(list(pipeline_result))
'''
Generator Pipeline Result:
[1, 9, 25]'''


#                                        qUESTION = 15.


class CustomIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.generator()

    def generator(self):
        current = self.start
        while current <= self.end:
            yield current
            current += 1



my_iterator = CustomIterator(1, 5)



for value in my_iterator:
    print(value)
    '''
1
2
3
4
5


                                                 QUESTION =16.'''


def generator_with_cleanup():
    try:
        for i in range(5):
            yield i
    except GeneratorExit:
        print("Generator is closing. Clean up if needed.")



my_generator = generator_with_cleanup()



for value in my_generator:
    print(value)


''''
my_generator.close()
0
1
2
3
4
Generator is closing. Clean up if needed.'''

#                                           QUESTION =17
def generator_with_exception_handling():
    try:
        while True:
            value = yield
            print("Received:", value)
    except Exception as e:
        print("Exception caught:", e)



my_generator = generator_with_exception_handling()



next(my_generator)



my_generator.send(1)
my_generator.send(2)



my_generator.throw(ValueError("Custom Exception"))
Received: 1
Received: 2


#                                               QUESTION =18.


import sys



def generator_sequence(n):
    for i in range(n):
        yield i



def list_sequence(n):
    return [i for i in range(n)]



generator_memory = sys.getsizeof(generator_sequence(1000000))
list_memory = sys.getsizeof(list_sequence(1000000))

print("Memory usage for generator:", generator_memory, "bytes")
print("Memory usage for list:", list_memory, "bytes")
'''
Memory usage for generator: 112 bytes
Memory usage for list: 9000112 bytes'''


#                                                          QUESTION =19.




import asyncio



async def asynchronous_generator():
    for i in range(5):
        await asyncio.sleep(1)  
        
        yield i



async def process_data():
    async for value in asynchronous_generator():
        print("Received:", value)



asyncio.run(process_data())
Received: 0
Received: 1
Received: 2
Received: 3
Received: 4


#                                                              QUESTION =20.


import itertools



count_generator = itertools.count(start=1, step=2)
values = list(next(count_generator) for _ in range(5))
print("Example 1:", values)



cycle_generator = itertools.cycle(['A', 'B', 'C'])
values = list(next(cycle_generator) for _ in range(8))
print("Example 2:", values)



iterable1 = range(3)
iterable2 = ['a', 'b', 'c']
chained_values = list(itertools.chain(iterable1, iterable2))
print("Example 3:", chained_values)
'''
Example 1: [1, 3, 5, 7, 9]
Example 2: ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B']
Example 3: [0, 1, 2, 'a', 'b', 'c']'''

#                                                QUESTION =21
import time

def task(name, times):
    for _ in range(times):
        print(f'Task {name} is running')
        yield  
        time.sleep(1)


def scheduler(tasks):
    while any(tasks):
        for task in tasks:
            try:
                next(task)
            except StopIteration:
                task.remove(task)
    

task1 = task('A', 3)
task2 = task('B', 4)



scheduler([task1, task2])
'''
Task A is running
Task B is running
Task A is running
Task B is running
Task A is running
Task B is running
Task B is running'''


#                                                       QUESTION =22.


def is_prime(num):
    
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


prime_gen = prime_generator()
primes = [next(prime_gen) for _ in range(5)]
[2, 3, 5, 7, 11]


#                                                  question =23.



def process_log_file(file_path):
    
    with open(file_path, 'r') as log_file:
        for line in log_file:

            
            processed_entry = process_log_entry(line)
            yield processed_entry

def process_log_entry(log_entry):

    
    return log_entry.strip().upper()



log_file_path = 'large_log_file.txt'
log_entries_generator = process_log_file(log_file_path)
first_5_entries = [next(log_entries_generator) for _ in range(5)]
['LOG ENTRY 1', 'LOG ENTRY 2', 'LOG ENTRY 3', 'LOG ENTRY 4', 'LOG ENTRY 5']


#                                            QUES24.


def fibonacci_generator():

    
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b



fibonacci_gen = fibonacci_generator()
first_5_fibonacci_numbers = [next(fibonacci_gen) for _ in range(5)]
'''
[0, 1, 1, 2, 3]'''
#                                             question =25
def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()



def filter_lines(lines, keyword):
    return (line for line in lines if keyword in line)



log_file_path = 'large_log_file.txt'



lines_generator = read_large_file(log_file_path)
filtered_lines_generator = filter_lines(lines_generator, 'error')


first_5_error_lines = [next(filtered_lines_generator) for _ in range(5)]
'''
['2022-01-01 12:01:30 - ERROR: Invalid input',
'2022-01-01 12:05:45 - ERROR: Connection failed',
'2022-01-01 12:10:20 - ERROR: File not found',
'2022-01-01 12:15:12 - ERROR: Server timeout',
'2022-01-01 12:20:05 - ERROR: Database error']'''