#                                          Question =1
def divide_numbers(a, b):
    try:
        result = a / b
        print("Division result:", result)
    except ZeroDivisionError as e:
        print("Error:", e)
    except TypeError as e:
        print("Error:", e)
    except Exception as e:
        print("Generic Error:", e)
    else:
        print("No exception occurred.")
    finally:
        print("This block always executes.")


divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers("10", 2)
'''
Output:

Division result: 5.0
Error: division by zero
Generic Error: unsupported operand type(s) for /: 'str' and 'int'
This block always executes.'''

#                                              Question =2
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
    '''
Output:

Error: division by zero'''
#                                               Question =3
try:
    
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    
    result = num1 / num2

except ZeroDivisionError as e:
    
    print("Error:", e)

except ValueError as e:
    
    print("Error:", e)

else:
    
    print("Result:", result)

finally:
    
    print("Execution complete.")
'''Output:

Enter the numerator: 10
Enter the denominator: 2
Result: 5.0'''


#                                               Question = 4
try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    
    result = num1 / num2

except ZeroDivisionError as e:
    print("Error:", e)

except ValueError as e:
    print("Error:", e)

else:
    print("Result:", result)

finally:
    print("Execution complete.")
'''Output (Example):

Enter the numerator: 10
Enter the denominator: 2
Result: 5.0'''
#                                                       Question = 5
def divide_numbers(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    else:
        return num1 / num2

try:
    result = divide_numbers(10, 0)

except ValueError as e:
    print("Error:", e)

else:
    print("Result:", result)
'''
Output (Example):

Error: Cannot divide by zero.'''
#                                                               qestion =6
def perform_division(num1, num2):
    try:
        result = num1 / num2

    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
        result = None

    return result
result1 = perform_division(10, 2)
result2 = perform_division(10, 0)
result3 = perform_division(10, "2")

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
'''
Output (Example):

Result 1: 5.0
Error: division by zero
Result 2: None
Error: unsupported operand type(s) for /: 'int' and 'str'
Result 3: None'''


#                                                            Question =7.


def perform_division(num1, num2):
    try:
        result = num1 / num2

    except ZeroDivisionError as e:
        print(f"Error: {e}")
        result = None

    finally:
        print("This block always gets executed.")
        

    return result


result1 = perform_division(10, 2)
result2 = perform_division(10, 0)

print("Result 1:", result1)
print("Result 2:", result2)
'''Output (Example):

This block always gets executed.
Result 1: 5.0
This block always gets executed.
Error: division by zero
Result 2: None'''


#                                         Question =8


class CustomError(Exception):
    def __init__(self, message="Custom error occurred"):
        self.message = message
        super().__init__(self.message)

def custom_function(value):
    try:
        if value < 0:
            raise CustomError("Negative value not allowed")

        
        result = 10 / value

    except CustomError as ce:
        print(f"CustomError: {ce}")

    else:
        print("No custom error occurred.")

    finally:
        print("Cleanup or finalization code here.")


custom_function(5)
custom_function(-2)
'''Output (Example):

No custom error occurred.
CustomError: Negative value not allowed
Cleanup or finalization code here.'''
#                                                    question =9
def divide_numbers(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        print("Cannot divide by zero!")

    else:
        print(f"The result of {a} divided by {b} is: {result}")

    finally:
        print("This code always runs, regardless of exceptions.")

# Example usage
divide_numbers(10, 2)
divide_numbers(10, 0)
'''Output (Example):

The result of 10 divided by 2 is: 5.0
Cannot divide by zero!
This code always runs, regardless of exceptions.
In this example, the divide_numbers function attempts to perform division in the try block. If a ZeroDivisionError occurs, the corresponding except block is executed. If no exception occurs, the else block is executed, printing the result. The finally block is always executed, providing a place for cleanup or finalization code.
'''
#                                                     Queston = 10.


try:
    
    x = 10 / 0

except ZeroDivisionError as e:
    print(f"Caught an exception: {type(e).__name__}, Message: {e}")




try:
    
    x = 10 / 0

except ZeroDivisionError, e:
    print("Caught an exception:", type(e).__name__, ", Message:", e)


11.

x = 10


assert x > 0, "The value of x is not positive"

print("Assertion passed: x is positive")


'''The output 

Assertion passed: x is positive'''



#                                                # Question = 12.


try:
    
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError as e:
    print(f"Error: {e}. The specified file was not found.")

except PermissionError as e:
    print(f"Error: {e}. Permission denied to access the file.")

except IOError as e:
    print(f"Error: {e}. An I/O error occurred while reading the file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("File read successfully.")

finally:
    print("File handling completed.")

'''The output :

Error: [Errno 2] No such file or directory: 'nonexistent_file.txt'. The specified file was not found.
File handling completed.'''
#                                                  # Question =13
try:
    # Open a file using with statement
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError as e:
    print(f"Error: {e}. The specified file was not found.")

except PermissionError as e:
    print(f"Error: {e}. Permission denied to access the file.")

except IOError as e:
    print(f"Error: {e}. An I/O error occurred while reading the file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("File read successfully.")

finally:
    print("File handling completed.")
    '''
The output will be:

Error: [Errno 2] No such file or directory: 'example.txt'. The specified file was not found.
File handling completed.'''
#                                           Question =14.


def example_function():
    try:
        
        x = 1 / 0

    except ZeroDivisionError as e:
        
        print(f"Caught an exception: {e}")

        
        raise

try:
    example_function()

except ZeroDivisionError as e:
    print(f"Exception propagated: {e}")
'''
The output :

Caught an exception: division by zero
Exception propagated: division by zer'''
#                                              Questiom = 15.


import sys

def example_function():
    try:
        
        x = 1 / 0

    except ZeroDivisionError as e:
        
        exc_type, exc_value, exc_traceback = sys.exc_info()

        
        print(f"Exception Type: {exc_type}")
        print(f"Exception Value: {exc_value}")
        print(f"Exception Traceback: {exc_traceback}")

try:
    example_function()

except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")


'''The output will be:

Exception Type: <class 'ZeroDivisionError'>
Exception Value: division by zero
Exception Traceback: <traceback object at 0x...>
Caught an exception: division by zero'''
#                                                Question =16.


def example_function(divisor):
    try:
        result = 10 / divisor

    except ZeroDivisionError:
        print("Cannot divide by zero!")

    else:
        print("Division successful. Result:", result)

    finally:
        print("This will always be executed, regardless of exceptions.")


example_function(2)
example_function(0)


'''The output will be:

Division successful. Result: 5.0
Cannot divide by zero!
This will always be executed, regardless of exceptions.
This will always be executed, regardless of exceptions.'''

#                                              Question =17
def example_function(divisor):
    try:
        result = 10 / divisor

    except (ZeroDivisionError, TypeError) as e:
        print(f"Exception caught: {type(e).__name__} - {e}")

    else:
        print("Division successful. Result:", result)

    finally:
        print("This will always be executed, regardless of exceptions.")


example_function(2)
example_function(0)
example_function("string")

'''
The output:

Division successful. Result: 5.0
Exception caught: ZeroDivisionError - division by zero
This will always be executed, regardless of exceptions.
Exception caught: TypeError - unsupported operand type(s) for /: 'str' and 'int'
This will always be executed, regardless of exceptions.'''
#                                        Questoion=18.



def divide(a, b):
    assert b != 0, "Division by zero is not allowed"
    return a / b


result = divide(10, 2)
print("Result:", result)



'''

Result: 5.0
'''

#                                               Question =19.


def divide(a, b):
    try:
        result = a / b
    except:
        print("An error occurred during division")


divide(10, 2)
divide(10, 0)


'''The output :

Result: 5.0
An error occurred during division'''


#                                                  Question =20.


import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)

def divide(a, b):
    try:
        result = a / b
    except Exception as e:
        
        logging.exception(f"An error occurred: {e}")


divide(10, 2)
divide(10, 0)


'''
The output :

ERROR:root:An error occurred: division by zero
Traceback (most recent call last):
  File "example.py", line 12, in divide
    result = a / b
ZeroDivisionError: division by zero'''




