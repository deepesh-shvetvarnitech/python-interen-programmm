'''                                           SECTION = 1
1) 5
2) for
3) for item in items:
4) 1 2 3 4 5
5) The condition is True
6) 0 1 2
7) break
8)Skips the current iteration and continues with the next iteration.
9) while
10) All of the above
11) Each letter on separate lines
12) Infinite loop
13) 1, 3, 5, 7, 9
14) 10 20 30
15) for
16) for
17) while
18) Indices only
19) Both index and value
20) for line in logs:
                                               SECTION = B
1(A)
for Loop
Used when the number of iterations is known.                                              
while Loop
Used when the number of iterations is unknown.
1(B)
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
user_input = ""

while user_input != "exit":
    user_input = input("Enter something (type 'exit' to stop): ")
    print(user_input)
        
2(A)
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
3
choice = ""

while choice != "quit":
    choice = input("Enter option (quit to exit): ")

    if choice != "quit":
        print("You selected:", choice)

print("Menu Closed")
4
numbers = [3, 7, 9, 8, 10]

for num in numbers:
    if num % 2 == 0:
        print(num)
        break
5
cart_items = [
    {"name": "Book", "price": 300},
    {"name": "Pen", "price": 50},
    {"name": "Notebook", "price": 200}
]

total_price = 0

for item in cart_items:
    total_price += item["price"]

print("Total Price:", total_price)

if total_price >= 500:
    discount = total_price * 0.10
else:
    discount = 0

final_price = total_price - discount

print("Discount:", discount)
print("Final Price:", final_price)
                                               SECTION=C
1
sum = 0

for i in range(1, 6):
    print(i)
    sum += i

print("Sum =", sum)
2
cart = ["book", "pen", "notebook"]

for item in cart:
    print(item)

for i, item in enumerate(cart):
    print(i, item)
     
3
name = "Alice"

for letter in name:
    print(letter)

print("Vowels:")

for letter in name:
    if letter.lower() in "aeiou":
        print(letter)
               
4
user_input = ""

while user_input != "exit":
    user_input = input("Enter text (type 'exit' to stop): ")

print("Program Ended")
5)
for i in range(1, 11):

    if i == 6:
        break

    if i % 2 == 0:
        continue

    print(i)
6)
marks = [75, 88, 92, 60, 77]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Total =", total)
print("Average =", average)
7)
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} *  {j} = {i * j}")   
                                                SECTION=4
1
cart_items = [
    ("Laptop", 49999),
    ("Mouse", 499),
    ("Keyboard", 1499)
]

subtotal = 0

for item, price in cart_items:
    subtotal += price
    print("Item:", item)
    print("Price:", price)
    print("Running Total:", subtotal)
    print()

if subtotal > 50000:
    discount = subtotal * 0.10
else:
    discount = 0

final_price = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Price:", final_price)

2
cart_items = [
    ("Laptop", 49999),
    ("Mouse", 499),
    ("Keyboard", 1499)
]

subtotal = 0

for item, price in cart_items:
    subtotal += price
    print("Item:", item)
    print("Price:", price)
    print("Running Total:", subtotal)
    print()

if subtotal > 50000:
    discount = subtotal * 0.10
else:
    discount = 0

final_price = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Price:", final_price)
                                                                                                                              '''
