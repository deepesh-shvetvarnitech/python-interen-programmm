'''                                              SECTION=A
1) list
2) my_list[1]
3) my_dict["name"]
4) "h"
5) The number of elements
6) At the end
7) Last element
8) First 2
9) The first 2
10) Uppercase
11) ["hello", "world"]
12) {"name": "Alice"}
13) A key
14) Values only
15) Keys
16) Substring
17) 0
18) Shopping cart
19) User profile
20) Processing user-input

                                              section =b
                                              question = 1
                                              (A)
 
Empty list: lst = []
List with values: lst = [10, 20, 30]
Append: lst.append(40) → Adds one element at the end.
Extend: lst.extend([50, 60]) → Adds multiple elements.
Remove: lst.remove(20) → Removes the first occurrence of 20.
Pop: lst.pop() → Removes the last element (or lst.pop(index) removes a specific index)

                                              (B)
lst[start:end] → Returns elements from start to end-1.
lst[::-1] → Returns the list in reverse order.
                                              (c)
cart = ["Laptop", "Mouse", "Keyboard"]

                                         Question =2
Create a dictionary: student = {"name": "Rahul", "age": 20}
Add/Update: student["city"] = "Delhi" or student["age"] = 21
Delete:
del student["city"]
student.pop("age") 
                                           (B)
Iterate:

Keys: for key in student:
Values: for value in student.values():
Items (key & value): for key, value in student.items():
                                            (C)
get() with default:

student.get("salary", 0)
Returns the value if the key exists; otherwise returns the default value (0).
                                           (D)
user = {
    "name": "Rahul",
    "age": 20,
    "city": "Delhi"
}
                                    Question =3
str is immutable, which means you cannot change individual characters after the string is created.
Indexing: text[0] → Returns the first character.
Slicing: text[start:end] → Returns a part of the string.
                                        (B)
upper() → Converts to uppercase.
lower() → Converts to lowercase.
strip() → Removes spaces from both ends.
split() → Splits a string into a list.
" ".join(list) → Joins list elements into a string.
replace(old, new) → Replaces one substring with another.
                                        (c)
data = "Rahul,20,Delhi"

details = data.split(",")

print(details)
                                  Question =4
Create an empty list: students = []
Each student is stored as a dictionary with "name", "age", and "marks".
Use append() to add students.
Use a for loop to search and print student details
                                     (B)
students = []

students.append({
    "name": "Rahul",
    "age": 20,
    "marks": 85
})

students.append({
    "name": "Priya",
    "age": 21,
    "marks": 92
})


search = "Rahul"

for student in students:
    if student["name"] == search:
        print(student)


print("\nAll Students:")
for student in students:
    print(student)                                                                                                                                                                                                                                                                                                                             
                                                  Question =5
Use split() to convert a sentence into a list of words.
Use a for loop to process each word.
Use upper() to print each word in uppercase.
                                                   (b)
text = "The quick brown fox jumps"

words = text.split()

for word in words:
    print(word.upper())                                                  
                                               section=c
                                               question=1

. Shopping Cart with list

cart = []


cart.append("laptop")
cart.append("mouse")
cart.append("keyboard")
print("Shopping Cart:")
for item in cart:
    print(item)


item_count = len(cart)
print("Total Items:", item_count)


                                              question =2
 User Profile with dict 

user = {
    "name": "Alice",
    "age": 25,
    "city": "Mumbai"
}


user["email"] = "alice@gmail.com"


user["city"] = "Delhi"


for key in user:
    print(key, ":", user[key])


print("Phone:", user.get("phone", "Not provided"))     
                                      question=3
 List of Student Records 

students = []


students.append({"name": "Rahul", "marks": 85})
students.append({"name": "Priya", "marks": 72})


print("Student Records:")

for student in students:
    print("Name:", student["name"])
    print("Marks:", student["marks"])


total = 0

for student in students:
    total = total + student["marks"]

average = total / len(students)

print("Average Marks:", average)

                                            question=4



log_line = "2024-05-24 INFO User login successful"


parts = log_line.split()


print("Level:", parts[1])


message = " ".join(parts[2:])
print("Message:", message)
Real-World Use (Log Parser)

                                         #question=5

 Product Catalog with list + dict (5 Marks)

products = []


products.append({"id": 1, "name": "Laptop", "price": 50000})
products.append({"id": 2, "name": "Phone", "price": 25000})


print("Product List:")

for product in products:
    print("Name:", product["name"])
    print("Price:", product["price"])


print("Products below 30000:")

for product in products:
    if product["price"] < 30000:
        print(product["name"], "-", product["price"])


                              question =6

name = input("Name: ").strip()
email = input("Email: ").strip()


if name != "" and "@" in email:

    user = {
        "name": name,
        "email": email
    }

    print("User Details:")
    print(user)

else:
    print("Invalid Name or Email")

                                         


                                         Question = 7
accounts = []


accounts.append({"acc_no": 101, "name": "Rahul", "balance": 15000})
accounts.append({"acc_no": 102, "name": "Priya", "balance": 8000})
accounts.append({"acc_no": 103, "name": "Amit", "balance": 22000})


print("Bank Records:")

for account in accounts:
    print("Account No:", account["acc_no"])
    print("Name:", account["name"])
    print("Balance:", account["balance"])
    print()


print("Accounts with Balance greater than 10000:")

for account in accounts:
    if account["balance"] > 10000:
        print(account["name"], "-", account["balance"])
                                              section = d
                                              Question=1

cart_items = []


products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 499}
]


selected_ids = [1, 2, 2]     

for pid in selected_ids:
    for product in products:
        if product["id"] == pid:

            found = False

            
            for item in cart_items:
                if item["id"] == pid:
                    item["quantity"] += 1
                    found = True
                    break

            
            if not found:
                cart_items.append({
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": 1
                })


subtotal = 0

for item in cart_items:
    item_total = item["price"] * item["quantity"]
    subtotal += item_total


discount = 0

if subtotal > 50000:
    discount = subtotal * 0.10

final_total = subtotal - discount


print("------ SHOPPING CART ------")

for item in cart_items:
    total = item["price"] * item["quantity"]

    print("Item :", item["name"])
    print("Quantity :", item["quantity"])
    print("Price :", item["price"])
    print("Total :", total)
    print()

print("Subtotal :", subtotal)
print("Discount :", discount)
print("Final Total :", final_total)  

                                        Question =2

students = [
    {"roll": 1, "name": "Rahul", "marks": [75, 80, 90]},
    {"roll": 2, "name": "Priya", "marks": [45, 50, 55]},
    {"roll": 3, "name": "Amit", "marks": [95, 90, 92]},
    {"roll": 4, "name": "Neha", "marks": [35, 40, 45]}
]

print("------ STUDENT REPORT ------")

for student in students:

    total = sum(student["marks"])
    average = total / len(student["marks"])

    if average >= 50:
        result = "Pass"
    else:
        result = "Fail"

    print("Roll :", student["roll"])
    print("Name :", student["name"])
    print("Marks :", student["marks"])
    print("Total :", total)
    print("Average :", average)
    print("Result :", result)
    print()                                                                                    










































































































'''
