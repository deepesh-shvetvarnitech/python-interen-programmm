'''                                              SECTION =A
1 — class
2 — __init__()
3 — Object
4 — __init__() using self
5 — String representation
6 — Hiding/internal implementation details
7 — Inheritance
8 — Child re-defining parent method
9 — Parent constructor
10 — Make method look like attribute
11— __name
12— Object type
13 — Vehicle → Car, Bike
14 — Different payment_method.process() for CreditCard, UPI
15 — User, Product, Order
16 — Current object
17 — Constructor
18 — Method call
19— "Product: Laptop, Price: 50000"
20— Modular, reusable code

#                                              SECTION =B
                                           QUESTION=1(A)
A class is a blueprint (template) for creating objects.

Real Life Example:

Blueprint of a house = Class
Actual house = Object

An object is a real instance of a class.

Example:

Class → User
Objects → Rahul, Deepesh, Priya
__init__() is a constructor.

It runs automatically when an object is created.

It initializes (gives values to) the object's variables.
                                             (B)

class User:

    
    def __init__(self, name, email):

        
        self.name = name

        
        self.email = email



user1 = User("Deepesh", "deepesh@gmail.com")


print(user1.name)
print(user1.email)      
                                            (C)
                                       #qUESTION=2
Encapsulation means

Data ko protect karna aur controlled access dena.
                                            (b)
class BankAccount:

    def __init__(self):
        self.balance = 5000

account = BankAccount()

print(account.balance)    
                                            QUESTION =3
Inheritance means

Child class inherits Parent class properties.
                                               (b)
 class Vehicle:

    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):

    def __init__(self, brand, model):

        super().__init__(brand)

        self.model = model


car = Car("Toyota", "Fortuner")

print(car.brand)
print(car.model)
                                             qUESTION = 4
 Polymorphism means

Same method name but different implementation.
                                                (B)
class Shape:

    def area(self):
        pass


class Circle(Shape):

    def area(self):
        return "Area of Circle"


class Rectangle(Shape):

    def area(self):
        return "Area of Rectangle"


circle = Circle()

rectangle = Rectangle()

print(circle.area())
print(rectangle.area())
                                                    qUESTION =5
# User class
class User:

    def __init__(self, name, email):

        self.name = name

        self.email = email

        self.accounts = []


# Bank Account class
class BankAccount:

    def __init__(self, account_id, balance):

        self.account_id = account_id

        self.balance = balance


    def deposit(self, amount):

        self.balance += amount


    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

        else:

            print("Insufficient Balance")



user = User("Deepesh", "deepesh@gmail.com")

account = BankAccount(101, 5000)


user.accounts.append(account)


account.deposit(2000)


account.withdraw(1000)


print(account.balance)   

                                          SECTION = C
                                          qUESTION=1
 
class User:

    
    def __init__(self, name, email):

        
        self.name = name

        
        self.email = email
    
    def __str__(self):

        return f"Name: {self.name}, Email: {self.email}"



user1 = User("Deepesh", "deepesh@gmail.com")

print(user1)            
                                        QUESTION=2

class BankAccount:

    
    def __init__(self, account_holder, account_number, balance):

        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    
    def deposit(self, amount):

        self.balance += amount

        print(f"₹{amount} Deposited")

    
    def withdraw(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            print(f"₹{amount} Withdrawn")

        else:

            print("Insufficient Balance")



account = BankAccount("Deepesh", 101, 5000)


account.deposit(2000)


account.withdraw(3000)



print("Balance:", account.balance)   

                                                   qUESTION =3

class Product:

    
    def __init__(self, name, price):

        self.name = name
        self.price = price



class Cart:
    def __init__(self):

        self.items = []

    
    def add_item(self, product, qty):

        self.items.append((product, qty))

    
    def show_cart(self):

        print("Cart Items")

        for product, qty in self.items:

            print(product.name, "-", qty, "x ₹", product.price)



laptop = Product("Laptop", 50000)
mouse = Product("Mouse", 500)


cart = Cart()

cart.add_item(laptop, 1)
cart.add_item(mouse, 2)

cart.show_cart()  
                                                   qUESTION=4


class Employee:


    def __init__(self, name, salary):

        self.name = name
        self.salary = salary



class Manager(Employee):

    
    def __init__(self, name, salary, team_size):

        
        super().__init__(name, salary)

        self.team_size = team_size

    
    def __str__(self):

        return f"Manager: {self.name}, Salary: ₹{self.salary}, Team Size: {self.team_size}"



manager = Manager("Deepesh", 80000, 10)


print(manager)  

                                                qUESTION=6

class Shape:

    
    def area(self):
        pass



class Circle(Shape):


    def __init__(self, radius):
        self.radius = radius

    
    def area(self):
        return 3.14 * self.radius * self.radius



class Rectangle(Shape):

    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    def area(self):
        return self.width * self.height



circle = Circle(5)
rectangle = Rectangle(10, 4)

shapes = [circle, rectangle]


for shape in shapes:
    print(shape.area())   

                                         qUESTION=7

class BankAccount:

    
    def __init__(self, balance):
        self.__balance = balance

    
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    
    @property
    def balance(self):
        return self.__balance


account = BankAccount(5000)


account.deposit(2000)


account.withdraw(1000)


print(account.balance)


print(account.__balance)                                                                                      

































































































































































































































































































































































































































































































'''