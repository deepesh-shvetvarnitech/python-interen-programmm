#                                          Question= 1
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_speak(dog))
print(animal_speak(cat))
'''
wouf
meaw
                                                          Question=2'''
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


math_obj = MathOperations()
result1 = math_obj.add(2, 3)
result2 = math_obj.add(2, 3, 4)

print(result1)
print(result2)
'''
TypeError: add() takes 3 positional arguments but 4 were given'''
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"


def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_speak(dog))
print(animal_speak(cat))
'''
dog bark
cat meaw
                                                Question =3'''

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"


def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_speak(dog))
print(animal_speak(cat))
'''Output:

Dog barks
Cat meows
                                             Question =4'''
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


math_obj = MathOperations()


result1 = math_obj.add(2, 3)
result2 = math_obj.add(2, 3, 4)

print(result1)
print(result2)
'''Output:

TypeError: add() takes 3 positional arguments but 4 were given'''
#                                                    Question =5
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def concatenate_strings(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += f"{key}: {value} "
    return result.strip()


sum_result = add_numbers(2, 3, 4, 5)


concat_result = concatenate_strings(first_name="John", last_name="Doe", age=30)

print(sum_result)
print(concat_result)
'''Output:

14
first_name: John last_name: Doe age: 30'''
#                                                  Question =6
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"


def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_speak(dog))
print(animal_speak(cat))
'''Output:

Dog barks
Cat meows
                                                  Question=7'''
def add_numbers(a, b=0, c=0):
    return a + b + c


result1 = add_numbers(2, 3)
result2 = add_numbers(2, 3, 4)

print(result1)
print(result2)
'''Output:

5
9'''
#                                                 Question=8
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


def print_area(shape):
    return shape.area()


circle = Circle(5)
square = Square(4)


area1 = print_area(circle)
area2 = print_area(square)

print(area1)
print(area2)
'''Output:

78.5
16
                                                      Question=9'''
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


def print_area(shape):
    return shape.area()


circle = Circle(5)
square = Square(4)


area1 = print_area(circle)
area2 = print_area(square)

print(area1)
print(area2)
'''Output:

78.5
16
                                                     Question = 10'''
class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


class Cat(Animal):
    def speak(self):
        return "Cat meows"


def animal_speak(animal):
    return animal.speak()


dog = Dog()
cat = Cat()


result1 = animal_speak(dog)
result2 = animal_speak(cat)

print(result1)
print(result2)
'''Output:

Dog barks
Cat meows
                                             Questipn =11'''
class Dog:
    def speak(self):
        return "Dog barks"

class Cat:
    def speak(self):
        return "Cat meows"


def animal_speak(animal):
    return animal.speak()


dog = Dog()
cat = Cat()


result1 = animal_speak(dog)
result2 = animal_speak(cat)

print(result1)
print(result2)
'''Output:

Dog barks
Cat meows'''
#                                               Question=12
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError("Unsupported operand type")

    
    def __str__(self):
        return f"Point({self.x}, {self.y})"


point1 = Point(1, 2)
point2 = Point(3, 4)


result1 = point1 + point2
result2 = point1 + 5

print(result1)
print(result2)
'''Output:

Point(4, 6)
Point(6, 7)
                                                   Question=13'''
class CustomList:
    def __init__(self, items):
        self.items = items

    
    def __len__(self):
        return len(self.items)

    
    def __getitem__(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            raise IndexError("Index out of range")


custom_list = CustomList([1, 2, 3, 4, 5])
length = len(custom_list)


element = custom_list[2]

print(length)
print(element)
'''Output:

5
3
                                                        Question=14
                                                        '''
class CustomContainer:
    def __init__(self, items):
        self.items = items

    
    def __len__(self):
        return len(self.items)


list_object = [1, 2, 3, 4, 5]
custom_container_object = CustomContainer([1, 2, 3, 4, 5])


length_of_list = len(list_object)
length_of_custom_container = len(custom_container_object)

print(length_of_list)
print(length_of_custom_container)
'''Output:

5
5'''
#                                                      Question=14
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y


result1 = MathOperations.add(5, 3)        
result2 = MathOperations.add("Hello, ", "World")   
result3 = MathOperations.add([1, 2, 3], [4, 5, 6])   

print(result1)
print(result2)
print(result3)
'''
8
Hello, World
[1, 2, 3, 4, 5, 6]'''

#                                                   Question=16
from functools import singledispatch


@singledispatch
def process_data(data):
    raise NotImplementedError("Unsupported data type")


@process_data.register(int)
def _(data):
    return f"Processing integer: {data}"

@process_data.register(str)
def _(data):
    return f"Processing string: {data}"

@process_data.register(list)
def _(data):
    return f"Processing list: {data}"


result1 = process_data(42)
result2 = process_data("Hello, World!")
result3 = process_data([1, 2, 3])

print(result1)
print(result2)
print(result3)
'''Output:

Processing integer: 42
Processing string: Hello, World!
Processing list: [1, 2, 3]'''
#                                                       Question =17
class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def speak(self):
        return "Dog barks"


class Cat(Animal):
    def speak(self):
        return "Cat meows"


def animal_speak(animal):
    return animal.speak()

animal1 = Animal()
dog = Dog()
cat = Cat()


result1 = animal_speak(animal1)  
result2 = animal_speak(dog)      
result3 = animal_speak(cat)     

print(result1)
print(result2)
print(result3)
'''Output:

Animal speaks
Dog barks
Cat meows
                                         Question =18'''
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


def print_area(shape):
    return shape.area()


circle = Circle(5)
square = Square(4)


result1 = print_area(circle)
result2 = print_area(square)

print(result1)
print(result2)
'''Output:

78.5
16'''
#                                                     Question =19
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

def animal_speak(animal):
    return animal.speak()


animal1 = Animal()
dog = Dog()
cat = Cat()


result1 = animal_speak(animal1)
result2 = animal_speak(dog)
result3 = animal_speak(cat)

print(result1)
print(result2)
print(result3)
'''Output:

Animal speaks
Dog barks
Cat meows
                                                  Question=20'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

def print_area(shape):
    return shape.area()


circle = Circle(5)
square = Square(4)


result1 = print_area(circle)
result2 = print_area(square)

print(result1)
print(result2)
'''Output:

78.5
16
                                                    Question =21'''
class Vehicle:
    def start_engine(self):
        raise NotImplementedError("start_engine method not implemented")

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"

def initiate_engine(vehicle):
    return vehicle.start_engine()


car = Car()
motorcycle = Motorcycle()


result1 = initiate_engine(car)
result2 = initiate_engine(motorcycle)

print(result1)
print(result2)
'''Output:

Car engine started
Motorcycle engine started
                                                 Question =22'''
class Shape:
    def area(self):
        raise NotImplementedError("area method not implemented")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

def calculate_area(shape):
    if not isinstance(shape, Shape):
        raise TypeError("Input must be an instance of Shape")
    return shape.area()


circle = Circle(5)
square = Square(4)

result1 = calculate_area(circle)
result2 = calculate_area(square)

print(result1)
print(result2)
'''Output:

78.5
16
                                              Question = 23'''
class Shape:
    def __init__(self, name="Shape", color="Black"):
        self.name = name
        self.color = color

    def display_info(self):
        return f"{self.color} {self.name}"

class Circle(Shape):
    def __init__(self, radius, color="Red"):
        super().__init__("Circle", color)
        self.radius = radius

    def display_info(self):
        return f"{super().display_info()}, Radius: {self.radius}"

class Square(Shape):
    def __init__(self, side, color="Blue"):
        super().__init__("Square", color)
        self.side = side

    def display_info(self):
        return f"{super().display_info()}, Side: {self.side}"


shape = Shape()
circle = Circle(radius=5)
square = Square(side=4, color="Green")


result1 = shape.display_info()
result2 = circle.display_info()
result3 = square.display_info()

print(result1)
print(result2)
print(result3)
'''Output:

Black Shape
Red Circle, Radius: 5
Green Square, Side: 4

                                                Question=24'''
def square_area(side):
    return side**2

def circle_area(radius):
    return 3.14 * radius**2

def calculate_area(shape, side_or_radius, area_function):
    return f"The area of the {shape} is {area_function(side_or_radius)}"


square_result = calculate_area("Square", 4, square_area)
circle_result = calculate_area("Circle", 5, circle_area)

print(square_result)
print(circle_result)
'''Output:

The area of the Square is 16
The area of the Circle is 78.5
                                             Question =25'''
class Shape:
    def area(self):
        raise NotImplementedError("area method not implemented")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

def calculate_area(shape):
    return shape.area()


circle = Circle(5)
square = Square(4)


result1 = calculate_area(circle)
result2 = calculate_area(square)

print(result1)
print(result2)
'''
Output:

78.5
16
                                    '''
