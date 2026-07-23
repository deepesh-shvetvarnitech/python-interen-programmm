#                                       QUESTION=1
class EncapsulationExample:
    def __init__(self):
        self.__private_var = 10  

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value


obj = EncapsulationExample()


print(obj.get_private_var())  

obj.set_private_var(20)
print(obj.get_private_var())            
'''
10
20'''
#                                        QUESTION = 2
class InformationHidingExample:
    def __init__(self):
        self.__private_var = 10  

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value


obj = InformationHidingExample()



print(obj.get_private_var())  

obj.set_private_var(20)
print(obj.get_private_var()) 
'''
10
20'''
#                                            QUESTION = 3
class EncapsulationExample:
    def __init__(self):
        self.__private_var = 10  
    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value


obj = EncapsulationExample()





print(obj.get_private_var())  

obj.set_private_var(20)
print(obj.get_private_var())
'''
10'''
#                                             QUESTON=4
class EncapsulationExample:
    def __init__(self):
        # Private attribute
        self.__private_var = 10

        # Protected attribute
        self._protected_var = 20

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value

    def get_protected_var(self):
        return self._protected_var

    def set_protected_var(self, value):
        self._protected_var = value


obj = EncapsulationExample()


print(obj.get_private_var())     
print(obj.get_protected_var())   


obj.set_private_var(30)
obj.set_protected_var(40)


print(obj.get_private_var())     
print(obj.get_protected_var())
'''
10
20
30
40'''
#                                               QUESTION =5
class MyClass:
    def __init__(self):
        
        self.public_var = 10

        
        self._protected_var = 20

    def get_protected_var(self):
        return self._protected_var

    def set_protected_var(self, value):
        self._protected_var = value


obj = MyClass()


print(obj.public_var)           
print(obj._protected_var)       


obj._protected_var = 30


print(obj.get_protected_var())

'''
10
20
30'''
#                                                  QUESTION = 6
class NameManglingExample:
    def __init__(self):
        
        self.__private_var = 10


obj = NameManglingExample()



print(obj._NameManglingExample__private_var)
'''
10'''
#                                                  QUESTON =7 
class ReadOnlyPropertiesExample:
    def __init__(self, initial_value):
        
        self.__value = initial_value

    @property
    def value(self):
        return self.__value


obj = ReadOnlyPropertiesExample(5)


print(obj.value)
'''
5'''

#                                               QUESTION =8
class AccessModifiersExample:
    def __init__(self):
        
        self.__private_var = 10

        
        self._protected_var = 20

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value

    def get_protected_var(self):
        return self._protected_var

    def set_protected_var(self, value):
        self._protected_var = value
obj = AccessModifiersExample()


print(obj.get_private_var())    
print(obj.get_protected_var())   


obj.set_private_var(30)
obj.set_protected_var(40)

print(obj.get_private_var())     
print(obj.get_protected_var())
'''
10
20
30
40'''
#                                                QUESTION = 9
class Car:
    def __init__(self, make, model, year):
        
        self.__make = make
        self.__model = model
        self.__year = year
        self.__is_running = False

    def start_engine(self):
        self.__is_running = True
        print("Engine started.")

    def stop_engine(self):
        self.__is_running = False
        print("Engine stopped.")

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def is_engine_running(self):
        return self.__is_running


my_car = Car("Toyota", "Camry", 2022)


print(f"Car: {my_car.get_year()} {my_car.get_make()} {my_car.get_model()}")
my_car.start_engine()
print(f"Is engine running? {my_car.is_engine_running()}")
my_car.stop_engine()
print(f"Is engine running? {my_car.is_engine_running()}")    
'''
Car: 2022 Toyota Camry
Engine started.
Is engine running? True
Engine stopped.
Is engine running? False'''                                   

#                                              QUESTON = 10
class BankAccount:
    def __init__(self, account_number, balance):
        
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount} units. New balance: {self.__balance} units.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} units. New balance: {self.__balance} units.")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance


account = BankAccount("123456789", 1000)


account.deposit(500)
account.withdraw(200)
print(f"Current balance: {account.get_balance()} units.")
'''
Deposited 500 units. New balance: 1500 units.
Withdrew 200 units. New balance: 1300 units.
Current balance: 1300 units.
'''
#                                            QUESTION = 11
class EncapsulationExample:
    def __init__(self):
        
        self.__private_var = 10

        
        self._protected_var = 20

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value

    def get_protected_var(self):
        return self._protected_var

    def set_protected_var(self, value):
        self._protected_var = value


obj = EncapsulationExample()


print(obj.get_private_var())     
print(obj.get_protected_var())   


obj.set_private_var(30)
obj.set_protected_var(40)


print(obj.get_private_var())     
print(obj.get_protected_var()) 
'''
10
20
30
40'''
#                                             QUESTION =12
class PropertyEncapsulationExample:
    def __init__(self, radius):
        
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def diameter(self):
        
        return 2 * self.__radius

    @property
    def area(self):
        
        return 3.14 * self.__radius**2


circle = PropertyEncapsulationExample(5)


print(f"Radius: {circle.radius}")          
print(f"Diameter: {circle.diameter}")       
print(f"Area: {circle.area}")  

'''
Radius: 5
Diameter: 10
Area: 78.5'''

#                                                 QUSTION =13
class EncapsulationWithGetterSetter:
    def __init__(self):
        
        self.__value = 0

    
    def get_value(self):
        return self.__value

    
    def set_value(self, new_value):
        if new_value >= 0:
            self.__value = new_value
        else:
            print("Value must be non-negative. Setting to 0.")


obj = EncapsulationWithGetterSetter()


print(f"Initial value: {obj.get_value()}")   


obj.set_value(10)


print(f"Updated value: {obj.get_value()}")    


obj.set_value(-5)


print(f"Value after invalid attempt: {obj.get_value()}")

'''
Initial value: 0
Updated value: 10
Value after invalid attempt: Value must be non-negative. Setting to 0.'''

#                                                  QUESTION =14
class EncapsulationWithProperties:
    def __init__(self):
        
        self._value = 0

    
    @property
    def value(self):
        return self._value

    
    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            print("Value must be non-negative. Setting to 0.")


obj = EncapsulationWithProperties()


print(f"Initial value: {obj.value}")   


obj.value = 10


print(f"Updated value: {obj.value}")    


obj.value = -5


print(f"Value after invalid attempt: {obj.value}")

#value: 0
#Updated value: 10
#Value after invalid attempt: Value must be non-negative. Setting to 0.''' 

#                                              QUESTION = 15

class OverusedEncapsulationExample:
    def __init__(self, value):
        
        self.__value = value

    def get_value(self):
        return self.__value

    
    def set_value(self, new_value):
        self.__value = new_value
obj = OverusedEncapsulationExample(42)


print(f"Value: {obj.get_value()}")   


obj.set_value(99)

print(f"Updated value: {obj.get_value()}")

'''
Value: 42
Updated value: 99'''

#                                          QUESTION =16
class PropertyDecoratorExample:
    def __init__(self, radius):

        self.__radius = radius

    
    @property
    def radius(self):
        return self.__radius

    
    @property
    def diameter(self):
        return 2 * self.__radius

    
    @property
    def area(self):
        return 3.14 * self.__radius**2


circle = PropertyDecoratorExample(5)


print(f"Radius: {circle.radius}")          
print(f"Diameter: {circle.diameter}")      
print(f"Area: {circle.area}")
'''
Radius: 5
Diameter: 10
Area: 78.5'''

#                                            QUESTION =17
class BankAccount:
    def __init__(self, account_number, balance):
    
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):

        return self.__balance

class Customer:
    def __init__(self, name, account):
        
        self.__name = name
        self.__account = account

    def display_balance(self):
        
        print(f"Account balance for {self.__name}: {self.__account.get_balance()}")


account1 = BankAccount("123456789", 1000)
customer1 = Customer("John Doe", account1)


customer1.display_balance()  


account1.deposit(500)


customer1.display_balance() 
'''
Account balance for John Doe: 1000
Account balance for John Doe: 1500'''

#                                            QUESTION =18
class ImmutableClass:
    def __init__(self, initial_value):
        # Private attribute
        self.__value = initial_value

    def get_value(self):
        
        return self.__value


obj = ImmutableClass(42)


print(f"Initial value: {obj.get_value()}")  



obj.get_value() = 99  


print(f"Value after invalid attempt: {obj.get_value()}") 
'''
Initial value: 42
Value after invalid attempt: 42'''

#                                             QUESTION = 19
class BankAccount:
    def __init__(self, account_number, balance):
        
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        
        self.__balance += amount

    def withdraw(self, amount):
        
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        
        return self.__balance


account = BankAccount("123456789", 1000)
print(f"Initial balance: {account.get_balance()}")  


account.withdraw(500)


print(f"Updated balance: {account.get_balance()}")
'''
Initial balance: 1000
Updated balance: 500'''

#                                                 QUESTION =20
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
    
        return self.__name

    def get_salary(self):
        
        return self.__salary

    def raise_salary(self, percentage):
        
        self.__salary *= (1 + percentage / 100)


employee1 = Employee("John Doe", 50000)


print(f"Employee: {employee1.get_name()}, Salary: {employee1.get_salary()}") 


employee1.raise_salary(10)


print(f"Updated Salary: {employee1.get_salary()}") 
'''
Employee: John Doe, Salary: 50000
Updated Salary: 55000'''
#                                             QUESTION =21
class SecureAccount:
    def __init__(self, account_number, balance):
        # Private attributes
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        
        return self.__account_number

    def get_balance(self):
        
        return self.__balance

    def deposit(self, amount):
        
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount or insufficient funds.")


account = SecureAccount("123456789", 1000)


print(f"Account Number: {account.get_account_number()}")  
print(f"Initial Balance: {account.get_balance()}")  



account.deposit(500)
account.withdraw(200)


print(f"Updated Balance: {account.get_balance()}")  
'''
Account Number: 123456789
Initial Balance: 1000
Updated Balance: 1300'''
#                                              QUESTION =22
class ShoppingCart:
    def __init__(self):
        
        self.__items = []

    def add_item(self, item):
        
        self.__items.append(item)

    def get_items(self):
        
        return self.__items


cart1 = ShoppingCart()
cart2 = ShoppingCart()


cart1.add_item("Item A")
cart1.add_item("Item B")


print(f"Items in cart1: {cart1.get_items()}")  


cart1.get_items().append("Item C")


print(f"Items in cart1 after unintended modification: {cart1.get_items()}")  


print(f"Items in cart2: {cart2.get_items()}")
'''
Items in cart1: ['Item A', 'Item B']
Items in cart1 after unintended modification: ['Item A', 'Item B', 'Item C']
Items in cart2: []'''
#                                          QUESTION = 23
class Animal:
    def __init__(self, name):
        
        self._name = name

    def make_sound(self):
        
        print("Generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        
        super().__init__(name)
        
        self.__breed = breed

    def make_sound(self):
        
        print("Bark")

    def get_breed(self):
    
        return self.__breed


animal = Animal("Generic Animal")
dog = Dog("Buddy", "Golden Retriever")


print(f"Animal name: {animal._name}") 
animal.make_sound()  


print(f"Dog name: {dog._name}")  
print(f"Dog breed: {dog.get_breed()}")  
dog.make_sound()  

'''
Animal name: Generic Animal
Generic animal sound
Dog name: Buddy
Dog breed: Golden Retriever
Bark'''

#                                        QUESTION = 24
class TemperatureConverter:
    def __init__(self, temperature, unit="Celsius"):
        
        self.__temperature = temperature
        self.__unit = unit

    def get_temperature(self):
        
        return self.__temperature

    def get_unit(self):
    
        return self.__unit

    def convert_to_celsius(self):
        
        if self.__unit == "Fahrenheit":
            self.__temperature = (self.__temperature - 32) * 5/9
            self.__unit = "Celsius"

    def convert_to_fahrenheit(self):
        
        if self.__unit == "Celsius":
            self.__temperature = self.__temperature * 9/5 + 32
            self.__unit = "Fahrenheit"


temperature_converter = TemperatureConverter(25, "Celsius")


print(f"Initial Temperature: {temperature_converter.get_temperature()} {temperature_converter.get_unit()}")



temperature_converter.convert_to_fahrenheit()


print(f"Updated Temperature: {temperature_converter.get_temperature()} {temperature_converter.get_unit()}")
'''
Initial Temperature: 25 Celsius
Updated Temperature: 77 Fahrenheit'''

#                                    QUESTION=25
from datetime import datetime


current_datetime = datetime.now()


year = current_datetime.year
month = current_datetime.month
day = current_datetime.day


print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
'''
Year: 2024
Month: 2
Day: 3'''


