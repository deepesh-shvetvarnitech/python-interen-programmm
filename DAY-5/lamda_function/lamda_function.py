#                      Question = 1
square = lambda x: x**2
result = square(5)
print(result)
'''
25
                        Question = 2'''
def square_regular(x):
    return x**2

result_regular = square_regular(5)
print(result_regular)

square_lambda = lambda x: x**2
result_lambda = square_lambda(5)
print(result_lambda)
'''
25
                        Question =3'''
square = lambda x: x**2


result = square(5)


print(result)
'''
25                      Question =4
'''
add_numbers = lambda x, y: x + y


result = add_numbers(3, 5)


print(result)
'''
8
                          Question=5'''
square = lambda x: x**2


result = square(5)


print(result)
''' 25
                         Question=6'''
add_numbers = lambda x, y: x + y


result = add_numbers(3, 5)


print(result)

'''
8
                       Quesstion = 7'''
def apply_function(func, numbers):
    return [func(x) for x in numbers]


numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_function(lambda x: x**2, numbers)


print(squared_numbers)
'''
[1, 4, 9, 16, 25]
                      Question = 8'''
#multi_expr_lambda = lambda x, y: x + y; print(x)
#lambda_with_statement = lambda x: print(x)
#complex_lambda = lambda x: x**2 if x % 2 == 0 else x**3
'''
                      Question = 9'''
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))


print(squared_numbers)
'''
[1, 4, 9, 16, 25]
                       Question = 10'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))


print(even_numbers)
'''
[2, 4, 6, 8, 10]
                       Question = 11'''
pairs = [(1, 5), (2, 3), (3, 8), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])


print(sorted_pairs)
'''
[(4, 1), (2, 3), (1, 5), (3, 8)]
                     Question = 11(B)
'''
words = ["apple", "banana", "kiwi", "orange"]
words.sort(key=lambda x: len(x))


print(words)
'''
['kiwi', 'apple', 'banana', 'orange']
                             question =12
'''
from functools import reduce


numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)


print(product)
'''
120
                            question = 13'''
double = lambda x: x * 2


result = double(5)


print(result)
'''10
                             Question =14'''
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(lambda x: x * 2, numbers))


print(doubled_numbers)
'''
[2, 4, 6, 8]
                              Question =B'''
words = ["apple", "kiwi", "banana", "orange"]
sorted_words = sorted(words, key=lambda x: len(x))


print(sorted_words)
'''
['kiwi', 'apple', 'banana', 'orange']
'''
#                             Question=15
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]


print(squares)
'''
[1, 4, 9, 16, 25]
                               question=16'''
power_functions = [lambda x, n=n: x**n for n in range(1, 6)]


number = 2
powers_of_two = [power_function(number) for power_function in power_functions]

print(powers_of_two)        
'''
[2, 4, 8, 16, 32]
                           question =17'''
from functools import reduce


numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)


print(product)       
'''
120
                           Question =18'''
logger_decorator = lambda func: lambda *args, **kwargs: (
    print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}"),
    func(*args, **kwargs),
    print(f"Function {func.__name__} execution complete")
)


@logger_decorator
def add_numbers(x, y):
    return x + y


result = add_numbers(3, 5)


print("Result:", result)
'''
Calling function add_numbers with arguments (3, 5) and keyword arguments {}
Function add_numbers execution complete
Result: 8
                                       Question =19'''
operations = [
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x**2
]


value = 3
results = [operation(value) for operation in operations]


print("Results:", results)         
'''
            Results: [4, 6, 9]
                                       Question =20'''
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]


result = list(map(lambda x, y: x + y, zip(list1, list2)))


print("Result:", result)
'''
Result: [6, 8, 10, 12]
                                      Question =21'''
curried_add = lambda x: lambda y: lambda z: x + y + z


add_partial = curried_add(1)(2)


result = add_partial(3)


print("Result:", result)
'''
result:6 
                                   Question = 22'''
global_variable = 10


lambda_function = lambda x: x + global_variable


result = lambda_function(5)


print("Result:", result)
'''
result : 15
                                 Question =23'''
conditional_lambda = lambda x: "Positive" if x > 0 else "Non-Positive"


result1 = conditional_lambda(5)
result2 = conditional_lambda(0)
result3 = conditional_lambda(-3)


print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
'''

Result 1: Positive
Result 2: Non-Positive
Result 3: Non-Positive'''
#                                Question=24
identity_function = lambda x: x


result1 = identity_function(5)
result2 = identity_function("Hello")
result3 = identity_function([1, 2, 3])


print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
'''
Result 1: 5
Result 2: Hello
Result 3: [1, 2, 3]'''
#                                 question=25
add = lambda x, y: x + y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y


result = divide(multiply(add(3, 5), 2), 4)


print("Result:", result)
#                                      (B)
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


result = divide(multiply(add(3, 5), 2), 4)


print("Result:", result)
'''
result:4.0'''