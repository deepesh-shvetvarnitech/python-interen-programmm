'''
                                                   # SECTION = A
1                                                   
ans=def
2
ans=greet()
3
ans = add(1, 2)
4
ans=Exits and sends value back
5
ans=Function body
6
ans=Default name
7
ans=func(1) and func(1, 2)
8
ans = Utility/validation helper
9
ans = Price and tax
10
ans =Input marks list, return grade
11
ans = Local variable
12
ans= Default rate
13
ans = With no parameters
14
ans = Abstract math logic
15
ans= Check if "@" exists
16
ans =Returns None
17
ans = Shopping-cart total
18
ans = greet("Alice")

19
ans =Avoid code duplication
20
ans =Testing and reuse 
                                            SECTION = B
                                                                                              
                                            question=1(a)
    
ans= def → Used to create a function.
Parameters → Variables that receive values when the function is called.
Body → Code inside the function that performs the task.
return → Sends the result back to the caller and ends the function.
          
                                                   1(B) 
def add(a, b):
    return a + b
                                                    1(c)
ans = return lets you reuse the result later.
print only displays the output.
                                         question =2
ans = def calc_tax(price, rate=0.1):
    return price * rate

print(calc_tax(1000))
print(calc_tax(1000, 0.18))
                                           Question =3
x = 10

def func():
    x = 5
    print(x)

func()
print(x)
o/p = 8
10
                                        Question =4
 def calculate_total(items, tax_rate=0.1):
    subtotal = sum(items)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total

items = [100, 200]
print(calculate_total(items))
                    
                                       Question =5
def validate_email(email):
    if email and "@" in email:
        return True
    return False

print(validate_email("abc@gmail.com"))
print(validate_email("abcgmail.com"))
                                      SECTION =C
                                       
                                     QUESTION=1
                                                  

def greet(name):
    print(f"Hello, {name}")

# Function call
greet("Alice")



def greet(name="Guest"):
    print(f"Hello, {name}")


greet()                              
                                     QUESTION =2

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


result = multiply(add(2, 3), 2)

print(result)    
                                      QUESTION =3

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


greet("Alice")
greet("Bob", "Hi")  
                                     QUESTION = 4

def calc_total(items, discount=0):
    subtotal = sum(items)
    discount_amount = subtotal * discount / 100
    final_total = subtotal - discount_amount
    return subtotal, discount_amount, final_total


items = [100, 200, 300]

subtotal, discount_amount, final_total = calc_total(items, 10)

print("Subtotal:", subtotal)
print("Discount:", discount_amount)
print("Final Total:", final_total)     
                                QUESTION =5

def compute_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 70:
        return "B"
    else:
        return "C"


marks = 85
print(compute_grade(marks))    
                        QUESTION =6
   
def is_valid_email(email):
    return email != "" and "@" in email


print(is_valid_email("alice@example.com"))
print(is_valid_email(""))      
                           QUESTION =7

def apply_tax(price, rate=0.1):
    return price * (1 + rate)


def print_final_price(base_price, tax_rate=0.1):
    final_price = apply_tax(base_price, tax_rate)
    print(f"Final Price: {final_price}")


print_final_price(1000, 0.15)     
                           SECTION =D

                           qUESTION =1

prices = [100, 200, 150]


def calc_subtotal(prices):
    return sum(prices)


def calc_discounted_total(prices, discount=10):
    subtotal = calc_subtotal(prices)
    discount_amount = subtotal * discount / 100
    final_total = subtotal - discount_amount
    return subtotal, discount_amount, final_total


def print_invoice(prices, discount=10):
    subtotal, discount_amount, final_total = calc_discounted_total(prices, discount)

    print(f"Subtotal: {subtotal}")
    print(f"Discount Amount: {discount_amount}")
    print(f"Final Total: {final_total}")


print_invoice(prices)     

                             QUESTION =2
student = {
    "name": "Rahul",
    "marks": [75, 80, 90]
}


def calc_avg_marks(marks):
    return sum(marks) / len(marks)


def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"


def generate_report(student):
    avg = calc_avg_marks(student["marks"])
    grade = get_grade(avg)

    report = {
        "name": student["name"],
        "avg": avg,
        "grade": grade
    }

    return report


print(generate_report(student))                             
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 '''                                                                                                                                                                                                                                                                                                                                        