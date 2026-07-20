#                                             Question =1
numbers = [1,2,3]
for num in numbers:
    print(num)
'''     1
2
3'''
#                                             Question = 1(B)
counter=0
while counter<5:
    print(counter)
    counter+=8




#QUESTION = 3
def factorial_with_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


result_for = factorial_with_for_loop(5)
print(result_for)

#sol=120
#question =3
numbers = [1, 2, 3, 4, 5]

print("Iterating over the list using a for loop:")
for num in numbers:
    print(num)
'''
Iterating over the list using a for loop:
1
2
3
4
5
 Question= 4'''
print("Printing numbers from 0 to 4 using range():")
for num in range(5):
    print(num)    
'''Printing numbers from 0 to 4 using range():
0
1
2
3
4
Qusstion=5'''
while True:
    print("This is an infinite loop")
# this is an in infite loop
5(b)
counter = 0
while counter < 5:
    print("This is iteration", counter + 1)
    counter += 1
'''This is iteration 1
This is iteration 2
This is iteration 3
This is iteration 4
This is iteration 5        
question=6'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num)
    if num == 5:
        print("Breaking the loop")
        break
'''
solutiin=1
2
3
4
5
Breaking the loop
question= 7'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        # Skip even numbers
        continue
    print(num)
'''
SOLTION=1
3
5
7
9
question=8'''
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
else:
    print("Loop completed successfully!")

# Example 2: Using else with a while loop
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed successfully!")
'''solution =1
2
3
4
5
Loop completed successfully!
0
1
2
3
4
Loop completed successfully!
question=9'''
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Element: {fruit}")
'''soltion= 
Index: 0, Element: apple
Index: 1, Element: banana
Index: 2, Element: orange
question=10
'''
for i in range(1, 6):
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}")
'''
SOLUTION = 
question = 11'''
for i in range(5):
    pass  


counter = 0
while counter < 3:
    pass  
    counter += 1        
'''solution = 
QESTIION = 12'''
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
'''SOLTION =Alice is 25 years old.
Bob is 30 years old.
Charlie is 22 years old.
QUESTION = 13'''                
numbers_range = range(5)
numbers_xrange = xrange(5)

print(f"Type of numbers_range: {type(numbers_range)}")
print(f"Type of numbers_xrange: {type(numbers_xrange)}")

print("Numbers from range():", list(numbers_range))
print("Numbers from xrange():", list(numbers_xrange))
'''SOL=Type of numbers_range: <class 'list'>
Type of numbers_xrange: <type 'xrange'>
Numbers from range(): [0, 1, 2, 3, 4]
Numbers from xrange(): [0, 1, 2, 3, 4]'''
#quuestion=14
numbers = [1, 2, 3, 4, 5]


iterator = iter(numbers)


print(next(iterator))  
print(next(iterator))  


for num in iterator:
    print(num)
'''solution =1
2
3
4
5'''
#question=15
count = 0

while True:
    print("Iteration:", count)
    count += 1

    
    if count >= 5:
        break    
'''
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
qestuon=16'''
for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print("Inside the loop at i =", i)
for j in range(5):
    if j == 2:
        print("Skipping iteration at j =", j)
        continue
    print("Inside the loop at j =", j)
for k in range(3):
    if k == 1:
        print("Doing nothing at k =", k)
        pass
    else:
        print("Inside the loop at k =", k)

'''
'''
#question =17
counter = 0

while counter < 5:
    print("Inside the loop, counter =", counter)
    counter += 1
else:
    print("Inside the else clause, loop condition is False.")
# Output:
# Inside the loop, counter = 0
# Inside the loop, counter = 1
# Inside the loop, counter = 2
# Inside the loop, counter = 3
# Inside the loop, counter = 4
# Inside the else clause, loop condition is False.
# qestion=18
print("Normal Loop:")
for i in range(5):
    print(i, end=" ")

print("\n")

print("Reverse Loop:")
for i in range(5, 0, -1):
    print(i, end=" ")     
# Output:
# Normal Loop:
# 0 1 2 3 4
# 
# Reverse Loop:
# 5 4 3 2 1
# question=19
numbers = [4, 2, 7, 1, 9, 5]


sorted_numbers = sorted(numbers)


print("Original List:", numbers)
print("Sorted List:", sorted_numbers)


print("\nUsing For Loop with Sorted List:")
for num in sorted_numbers:
    print(num, end=" ")

# Output:
# Original List: [4, 2, 7, 1, 9, 5]
# Sorted List: [1, 2, 4, 5, 7, 9]
# 
# Using For Loop with Sorted List:
# 1 2 4 5 7 9  
# question =20
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)  

