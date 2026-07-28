#                                  Question =1
import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5, "Should be 5")

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5, "Should be -5")

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1, "Should be -1")

if __name__ == '__main__':
    unittest.main()
'''Outputs:

..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK'''


#                                            Question =2.


import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5, "Should be 5")

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5, "Should be -5")

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1, "Should be -1")

if __name__ == '__main__':
    unittest.main()
    '''output
..
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK'''

#                                                 (B)

import unittest

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

class TestIntegration(unittest.TestCase):
    def test_add_and_multiply(self):
        result = add(2, 3) * 4
        self.assertEqual(result, 20, "Should be 20")

if __name__ == '__main__':



#                                                Question =3.





 import unittest



def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5, "Should be 5")

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5, "Should be -5")

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1, "Should be -1")



if __name__ == '__main__':
    unittest.main()
'''Outputs:

...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK'''






#                                            Question =4.





import unittest



def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5, "Should be 5")

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5, "Should be -5")

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1, "Should be -1")


if __name__ == '__main__':
    unittest.main()
'''Outputs:

...
----------------------------------------------------------------------
Ran 3 tests in 0.000s
'''

#                                            Question =5
import unittest



def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def setUp(self):

        
        print("Setting up test...")

    def tearDown(self):

       
        print("Tearing down test...")

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5, "Should be 5")

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5, "Should be -5")

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1, "Should be -1")


if __name__ == '__main__':
    unittest.main()
'''Outputs:

.Setting up test...
.
Tearing down test...
.Setting up test...
.
Tearing down test...
.Setting up test...
.
Tearing down test...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK'''
#                                     Question =6
import unittest


def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5, "Should be 5")

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5, "Should be -5")

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1, "Should be -1")

'''output
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK'''

#                                      Question =7
import unittest



def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def setUp(self):

        
        self.num1 = 2
        self.num2 = 3

    def test_add_positive_numbers(self):
        result = add(self.num1, self.num2)
        self.assertEqual(result, 5, "Should be 5")

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5, "Should be -5")

    def test_add_mixed_numbers(self):
        result = add(self.num1, -3)
        self.assertEqual(result, -1, "Should be -1")


if __name__ == '__main__':
    unittest.main()
'''Outputs:

...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK'''

#                                 Question =8
import unittest


def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def setUp(self):

        
        self.num1 = 2
        self.num2 = 3

    def tearDown(self):

        
        print("Tearing down test...")

    def test_add_positive_numbers(self):
        result = add(self.num1, self.num2)
        self.assertEqual(result, 5, "Should be 5")

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5, "Should be -5")

    def test_add_mixed_numbers(self):
        result = add(self.num1, -3)
        self.assertEqual(result, -1, "Should be -1")



if __name__ == '__main__':
    unittest.main()
'''Outputs:

...
Tearing down test...
.
Tearing down test...
.
Tearing down test...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK'''
#                                            Question = 9
import unittest



def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(2, 3)

        
        assert result == 5, "Should be 5"

    def test_add_negative_numbers(self):
        result = add(-2, -3)

        
        assert result == -5, "Should be -5"

    def test_add_mixed_numbers(self):
        result = add(2, -3)

        
        assert result == -1, "Should be -1"



if __name__ == '__main__':
    unittest.main()
'''Outputs:

F.F
======================================================================
FAIL: test_add_positive_numbers (__main__.TestAddition)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_script.py", line 8, in test_add_positive_numbers
    assert result == 5, "Should be 5"
AssertionError: Should be 5

======================================================================
FAIL: test_add_mixed_numbers (__main__.TestAddition)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_script.py", line 18, in test_add_mixed_numbers
    assert result == -1, "Should be -1"
AssertionError: Should be -1

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=2)'''
 #                                      Question =10
def add(a, b):
    return a + b

def test_addition():
    assert add(2, 3) == 5, "Should be 5"

if __name__ == '__main__':
    test_addition()
'''Output:

No output if the test passes successfully'''

#                                       Questiom = 11
def add(a, b):
    return a + b

def test_add_positive_numbers():
    result = add(2, 3)
    assert result == 5, "Should be 5"

def test_add_negative_numbers():
    result = add(-2, -3)
    assert result == -5, "Should be -5"

def test_add_mixed_numbers():
    result = add(2, -3)
    assert result == -1, "Should be -1"
'''
============================= test session starts ==============================


collected 3 items                                                             

test_example.py ...                                                        [100%]

============================= 3 passed in 0.12s ==============================='''



#                                                     Quetion = 12.





def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


    
def test_add_positive_numbers():
    result = add(2, 3)
    assert result == 5, "Should be 5"

def test_add_negative_numbers():
    result = add(-2, -3)
    assert result == -5, "Should be -5"

def test_add_mixed_numbers():
    result = add(2, -3)
    assert result == -1, "Should be -1"


    
def test_subtract_positive_numbers():
    result = subtract(5, 3)
    assert result == 2, "Should be 2"

def test_subtract_negative_numbers():
    result = subtract(-2, -3)
    assert result == 1, "Should be 1"

def test_subtract_mixed_numbers():
    result = subtract(2, -3)
    assert result == 5, "Should be 5"



'''
Output:

============================= test session starts ==============================
...

collected 6 items                                                             

test_math_operations.py ......                                          [100%]

============================= 6 passed in 0.15s ==============================='''

#                                               Question =13




def setup_numbers():
    num1 = 2
    num2 = 3
    return num1, num2


def test_addition(setup_numbers):
    num1, num2 = setup_numbers
    result = add(num1, num2)
    assert result == 5, "Should be 5"

def test_subtraction(setup_numbers):
    num1, num2 = setup_numbers
    result = subtract(num1, num2)
    assert result == -1, "Should be -1"
    '''
    output
    ============================= test session starts ==============================
...

collected 2 items                                                             

test_fixture_example.py ..                                               [100%]

============================= 2 passed in 0.15s ===============================
                                                     Question =14'''
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def test_add_positive_numbers():
    result = add(2, 3)
    assert result == 5, "Should be 5"

def test_add_negative_numbers():
    result = add(-2, -3)
    assert result == -5, "Should be -5"

def test_subtract_positive_numbers():
    result = subtract(5, 3)
    assert result == 2, "Should be 2"

def test_subtract_negative_numbers():
    result = subtract(-2, -3)
    assert result == 1, "Should be 1"
    '''
    Output:

============================= test session starts ==============================
...

collected 4 items                                                             

test_selective_example.py ....                                          [100%]

============================= 4 passed in 0.15s ==============================='''
#                                                       question =15
from unittest.mock import Mock

def calculate_total_price(product, quantity, price_fetcher):
    unit_price = price_fetcher.get_price(product)
    return unit_price * quantity

def test_calculate_total_price():

    
    price_fetcher_mock = Mock()


    
    price_fetcher_mock.get_price.return_value = 10


    
    result = calculate_total_price("example_product", 3, price_fetcher_mock)


    
    price_fetcher_mock.get_price.assert_called_once_with("example_product")


    
    assert result == 30, "Should be 30"
    '''
    Output:

============================= test session starts ==============================
...

collected 1 item                                                              

test_mock_example.py .                                                  [100%]

============================= 1 passed in 0.15s ==============================='''
#                                              Question =16
def calculate_total_price(product, quantity, price_fetcher):
    unit_price = price_fetcher.get_price(product)
    return unit_price * quantity
def calculate_total_price(product, quantity, price_fetcher):
    if quantity < 0:
        raise ValueError("Quantity must be non-negative")

    unit_price = price_fetcher.get_price(product)
    if unit_price < 0:
        raise ValueError("Unit price must be non-negative")

    return unit_price * quantity
#                                          Question =17
import unittest



def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



class TestExceptionSimulation(unittest.TestCase):

    
    def test_divide_by_zero_exception(self):
        with self.assertRaises(ValueError) as context:

            
            result = divide(10, 0)


       
        self.assertEqual(str(context.exception), "Cannot divide by zero")


    
    def test_divide_non_numeric_exception(self):
        with self.assertRaises(TypeError):

            
            result = divide("10", 2)

if __name__ == '__main__':
    unittest.main()
'''
output
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK'''
#                                       Question =18
def add(a, b):
    if a > 0:
        return a + b
    else:
        return b




import unittest


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5, "Should be 5")

    def test_add_negative_numbers(self):
        result = add(-2, 3)
        self.assertEqual(result, 3, "Should be 3")

if __name__ == '__main__':
    unittest.main()
'''
output
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
example_module.py       5      1    80%   4
test_example_module.py  11      0   100%
--------------------------------------------------
TOTAL                   16      1    94%'''
#                                            Question =19
def add(a, b):

    
    return a + b

if __name__ == "__main__":

    
    import doctest
    doctest.testmod()
    '''
    output
    Trying:
    add(2, 3)
Expecting:
    5
ok
Trying:
    add(-2, 3)
Expecting:
    1
ok
Trying:
    add(0, 0)
Expecting:
    0
ok
1 items had no tests:
    example_module
1 items passed all tests:
   3 tests in example_module.add
3 tests in 2 items.
3 passed and 0 failed.
Test passed.'''
#                                Question =20
def add(a, b):
    return a + b



import unittest


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5, "Should be 5")

    def test_add_negative_numbers(self):
        result = add(-2, 3)
        self.assertEqual(result, 1, "Should be 1")