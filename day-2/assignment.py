'''
SECTION A :
1
ANNS=A VARIABLE HOLDING AN INTEGER
2
ANS = my_age
3
ans = FLOAT
4
ans = bool
5
ans = int
6
ans = set
7
ans = string
8
ans = list
9
ans= set
10 
ans = dic
11
ans = 2 items
12
ans = 5
13
ans = memory address
14
ans = x=10; x= "hello
15
ans = you canchange element using index
16
ans = you canot change element without using index
17
ans = its a boolean
18 
ans = simple user account model
19
ans = eccomerce product catalog
20
ans  = true'''
''' 
 SECTION : B
 1
 A = A variable is a named reference to a value stored in memory.
 B =Names must start with a letter (A-Z, a-z) or an underscore (_), never a digit.and no special character or space allowed
 c = No, they are completely different. Python variable names are strictly case-sensitive.
 2
 A =int: age (e.g., 25)float: price (e.g., 19.99)str: name (e.g., "Alice")bool: is_logged_in (e.g., True)list: shopping_cart (e.g., ["apple", "banana", "milk"])tuple: gps_coordinates (e.g., (40.7128, -74.0060))dict: user_profile (e.g., {"username": "coder123", "email": "abc@email.com"})set: unique_tags (e.g., {"python", "coding", "tutorial"})
 3
 a= Mutable: Objects that can be modified after creation.
 Immutable: Objects that cannot be altered once created.
 b =Mutable: list, dict, set
 Immutable: str, tuple, int
 c = list is mutable: You can add, remove, or change items in place without changing its memory address.
 tuple is immutable: Its size and contents are locked at creation; changing elements requires creating an entirely new tuple.
  d  =
age = 25


print("Type:", type(age))
print("ID:", id(age))

# question =5
# Student record assignment
roll_no = 101
name = "Deepesh Chouhan"
marks = [85, 92, 78, 90]
is_passed = True
#question = 6
product_1 = {"name": "Wireless Mouse", "price": 24.99, "quantity": 1}
product_2 = {"name": "USB-C Cable", "price": 9.99, "quantity": 2}


cart_items = [product_1, product_2]

SECTION = C 
QUESTION = 1
quantity = 10
price = 19.99
total = quantity * price
is_discounted = True


print("quantity:", quantity, "-> Type:", type(quantity))
print("price:", price, "-> Type:", type(price))
print("total:", total, "-> Type:", type(total))
print("is_discounted:", is_discounted, "-> Type:", type(is_discounted))

UESTION =2

name = "Alice"
hobbies = ["reading", "drawing"]


upper_name = name.upper()
hobbies.append("coding")


print("name:", name)
print("upper_name:", upper_name)
print("hobbies:", hobbies)

QUESTION = 3
- product = {"name": "Laptop", "price": 49999.0, "in_stock": True}


for key, value in product.items():
    print(f"Key: {key:9} | Value: {value:9} | Type: {type(value)}")
    QUESTION = 4
    record = [1, "Alice", 78.5, True]


for element in record:
    print(f"Element: {str(element):7} | Type: {type(element)}")

    QUESTION =5
    tags = {"python", "DSA", "python"}


print("Set contents:", tags)
print("Length of set:", len(tags))

QUESTION =6 
lst = [1, 2]
tup = (1, 2)


lst.append(3)
print("Modified list:", lst)


print("Unchanged tuple:", tup)

QUESTION =2(A)
student_id = 1001
name = "DEEPESH CHOUHAN"
subjects = ["Mathematics", "Physics", "Computer Science"]
marks = [85, 92, 78]
is_active = True
QUESTION = 2(B)
student_id = 1042
name = "DeepESH CHOUHNA"
subjects = ["Physics", "Chemistry", "Mathematics"]
marks = [58, 72, 65]
is_active = True


total_marks = sum(marks)


is_passed = total_marks >= 150


print(f"Student: {name}")
print(f"Total Marks Scored: {total_marks}")
print(f"Passed the Examination: {is_passed}")

SECTION = D  
income = 5000.00
expenses = [1200.50, 45.00, 350.00, 85.25, 650.00]


category_map = {
    "Rent": 1200.50,
    "Utilities": 85.25,
    "Groceries": 350.00,
    "Entertainment": 45.00,
    "Savings/Investments": 650.00
}


expense_sum = sum(expenses)


is_over_budget = expense_sum > income


print("--- FINANCIAL SUMMARY ---")
print(f"Monthly Income:   ${income:.2f}")
print(f"Total Expenses:   ${expense_sum:.2f}")
print(f"Over Budget?      {is_over_budget}")
print("-" * 25)
print("Category Breakdown:")
for category, amount in category_map.items():
    print(f" * {category:20}: ${amount:.2f}")'''