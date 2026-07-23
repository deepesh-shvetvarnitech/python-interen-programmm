#                                                Qustion=1
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"


dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")


print(dog_instance.name)  
print(dog_instance.make_sound())  

print(cat_instance.name)  
print(cat_instance.make_sound())  
'''
Buddy
Woof!
Whiskers
Meow!'''
#                                             Question=2
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"


dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")


animal_instance = Animal("Generic Animal")
print(animal_instance.name)  
print(animal_instance.make_sound())  

print(dog_instance.name)  
print(dog_instance.make_sound())  

print(cat_instance.name)  
print(cat_instance.make_sound())  
'''
Generic Animal
Generic animal sound
Buddy
Woof!
Whiskers
Meow!'''
#                                                  Question ==3
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        return f"Drawing a {self.color} shape"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        return f"Drawing a {self.color} circle with radius {self.radius}"

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def draw(self):
        return f"Drawing a {self.color} square with side length {self.side_length}"


circle_instance = Circle("Red", 5)
square_instance = Square("Blue", 4)


print(circle_instance.draw())  
print(square_instance.draw())
'''Drawing a Red circle with radius 5
Drawing a Blue square with side length 4
'''
#                                             Question = 4
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Woof!"


dog_instance = Dog("Buddy", "Labrador")


print(dog_instance.name)  
print(dog_instance.breed)  
print(dog_instance.make_sound())  
'''
Buddy
Labrador
Woof!'''
#                                              Question = 5
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Woof!"


dog_instance = Dog("Buddy", "Labrador")


print(dog_instance.name)  
print(dog_instance.breed)  
print(dog_instance.make_sound())
'''
Buddy
Labrador
Woof!'''
#                                          Question = 6
#                                       MULTIPLE INHERITANCE
class FirstClass:
    def method(self):
        return "Method from FirstClass"

class SecondClass:
    def method(self):
        return "Method from SecondClass"

class MultipleDerivedClass(FirstClass, SecondClass):
    def derived_method(self):
        return "Method from MultipleDerivedClass"

#                                        SINGLE INHERITANCE
class Animal:
    def speak(self):
        return "Generic animal sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"


class Bird:
    def chirp(self):
        return "Chirp"

class Parrot(Animal, Bird):
    def fly(self):
        return "Parrot flying"    

parrot_instance = Parrot()
print(parrot_instance.speak())  
print(parrot_instance.chirp())  
print(parrot_instance.fly())
''' GENRIC ANIMAL SOUND
CHIRP 
PARROT FLYONG'''
#                                                    Questiion =7
class Animal:
    pass

class Dog(Animal):
    pass

dog_instance = Dog()

print(isinstance(dog_instance, Dog))    
print(isinstance(dog_instance, Animal)) 
print(isinstance(dog_instance, str))
'''
true
true
false'''

class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))    

print(issubclass(Animal, Dog))    

print(issubclass(Dog, object)) 
'''
true
false
true'''

#                                                    Question = 8
class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"



animal_instance = Animal()
dog_instance = Dog()



print(animal_instance.make_sound())  

print(dog_instance.make_sound())  

'''
Generic animal sound
wolf!'''

#                                                    Question = 9
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return "Woof!"


dog_instance = Dog("Buddy", "Labrador")


print(dog_instance.name)   
print(dog_instance.breed)
'''
budddy 
labrador'''

#                                                   Question =10
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):
    pass



mro_sequence = D.__mro__



d_instance = D()



print(d_instance.show())  
'''
B'''
#                                                   Question =11
class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self):
        
        super_sound = super().make_sound()
        return f"{super_sound} and Woof!"


dog_instance = Dog()


print(dog_instance.make_sound())
'''
Generic animal sound and woulf'''

#                                                 Question =12
class Animal:
    total_animals = 0

    def __init__(self):
        Animal.total_animals += 1

    @classmethod
    def get_total_animals(cls):
        return cls.total_animals

class Dog(Animal):
    pass

class Cat(Animal):
    pass


dog_instance = Dog()
cat_instance = Cat()


total_animals = Animal.get_total_animals()

print(total_animals)
#                                    output = 2
#                                                Question =13
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length**2

    def perimeter(self):
        return 4 * self.side_length


circle_instance = Circle(5)
square_instance = Square(4)


circle_area = circle_instance.area()
circle_perimeter = circle_instance.perimeter()

square_area = square_instance.area()
square_perimeter = square_instance.perimeter()

print(circle_area)       
print(circle_perimeter)  

print(square_area)       
print(square_perimeter)
'''
78.5
31.4000000000000002
16
16'''
#                                               Question =14
class MathOperations:
    def calculate(self, *args):
        if len(args) == 2:
            return self.add(args[0], args[1])
        elif len(args) == 3:
            return self.multiply(args[0], args[1], args[2])
        else:
            return "Invalid number of arguments"

    def add(self, a, b):
        return a + b

    def multiply(self, a, b, c):
        return a * b * c


math_instance = MathOperations()


result_add = math_instance.calculate(5, 3)
result_multiply = math_instance.calculate(2, 4, 3)

print(result_add)       
print(result_multiply)  
'''
8
24'''
#                                                 Question =15
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(1, 2)
point2 = Point(1, 2)
point3 = point1


result_equal = point1 == point2


result_identical = point1 is point2
result_same_reference = point1 is point3


print(result_equal)           
print(result_identical)     
print(result_same_reference) 
'''
true
false
true'''
#                                             Question = 16
from final_class import final


@final
class BaseClass:
    def final_method(self):
        return "This method is final and cannot be overridden"


class SubClass(BaseClass):
    def final_method(self):
        return "This method attempts to override the final method"


subclass_instance = SubClass()


output = subclass_instance.final_method()

print(output)
'''
TypeError: Cannot override final method 'final_method'''
#                                          Question =17
class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"


def animal_sound(animal_instance):
    return animal_instance.make_sound()


dog_instance = Dog()
cat_instance = Cat()
result_dog = animal_sound(dog_instance)
result_cat = animal_sound(cat_instance)

print(result_dog)  
print(result_cat)
'''
woof!
meaw!'''
#                                            Question =18
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

class Calculator(MathOperations):
    def calculate(self, x, y):
        
        sum_result = self.add(x, y)
        product_result = self.multiply(x, y)
        return f"Sum: {sum_result}, Product: {product_result}"


calculator_instance = Calculator()


result = calculator_instance.calculate(3, 4)

print(result)

# sum: 7 product:12
#                                          Question =19
class Animal:
    def make_sound(self):
        return "Generic animal sound"

class Mammal(Animal):
    def give_birth(self):
        return "Live birth"

class Bird(Animal):
    def lay_eggs(self):
        return "Lay eggs"

class Platypus(Mammal, Bird):
    pass


platypus_instance = Platypus()


sound_result = platypus_instance.make_sound()

try:
    birth_result = platypus_instance.give_birth()
except AttributeError as e:
    birth_result = f"AttributeError: {e}"

try:
    eggs_result = platypus_instance.lay_eggs()
except AttributeError as e:
    eggs_result = f"AttributeError: {e}"

print(eggs_result) 
'''
Generic animal sound
AttributeError: 'Platypus' object has no attribute 'give_birth'
AttributeError: 'Platypus' object has no attribute 'lay_eggs
                                            Question =20'''
class Animal:
    def __init__(self):
        print("Animal constructor")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal constructor")

class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("Bird constructor")

class Platypus(Mammal, Bird):
    def __init__(self):
        super().__init__()
        print("Platypus constructor")


platypus_instance = Platypus()
'''
Animal constructor
Bird constructor
Mammal constructor
Platypus constructor'''