'''
                               SECTION=A
1
ANS=IF
2
ANS=INTENTED
3
ANS=ELIF
4
ANS= IF>=18:PRINT("ADULT")
5
ANS= RES= "HIGH"IF A>B ELSE "LOW"
6
ANS = BETWEEN 10 AND 20
7
ANS= NEGATIVE AND GREATER THEN 100
8
ANS= IF IS FALSE
9
ANS = IF INSIDE IF
10
ANS = TERNARY OPERATOR
11
ANS=DISCOUNT CALCUATOR
12
ANS = BAMK WITHDRAW ELIGIBLITY
13
ANS = STORE OPENHOURSE
14
ANS =TEMP -ALERT SYSTEM
15
ANS= PRIME-ONLY EVENING DISCIUNT
16
ANS = INVALID
17
ANS = PASSWORD VALIDATION BANK
18
ANS=ONE LINE CONDITIONALED
19
ANS=SORTING
  
SECTION=B


1                                         A
if condition_1:
    
elif condition_2:
    
else:
    
                                          B
number = -5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
                                        2

has_ticket = True
has_id = True
can_enter = has_ticket and has_id  


is_weekend = True
is_holiday = False
can_sleep_in = is_weekend or is_holiday  


is_raining = False
go_outside = not is_raining  # True
                                       B
 age = 20
has_license = True

if age >= 18 and has_license:
    print("User is eligible to drive.")
else:
    print("User is not eligible.")
                                        3
If marks >= 50:
    If attendance >= 75:
        Status: Approve
    Else:
        Status: Probation
Else:
    Status: Fail
                                       4
category = "Adult" if age >= 18 else "Minor"
                                      5
if price > 500:
    discount = price * 0.10
    final_price = price - discount
else:
    discount = price * 0.05
    final_price = price - discount
                               SECTION = C
                                1
    age = 19

if age >= 18:
    print("eligible to drive")
else:
    print("not eligible to drive")
                            
                                 2
  marks = 68

if marks >= 90:
    print("Distinction")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
                               3

year = 2024


if (year % 400 == 0):
    print("Leap Year")
elif (year % 100 == 0):
    print("Not a leap year")
elif (year % 4 == 0):
    print("Leap Year")
else:
    print("Not a leap year")
                             4
 temp = 42

if temp > 40:
    print("Heat Alert")
elif temp < 0:
    print("Cold Alert")
else:
    print("Normal Weather")
                              5

balance = 1000
withdraw = 750


if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")
                               6
price = 600


if price > 1000:
    final = price * 0.80      # 20% discount
    discount = "20%"
elif price > 500:
    final = price * 0.90      # 10% discount
    discount = "10%"
else:
    final = price * 0.95      # 5% discount
    discount = "5%"


print("Original Price:", price)
print("Discount Applied:", discount)
print("Final Price:", final)       
                              7

password = "secure123"
input_password = "wrong"


if input_password == password:
    print("Access granted")
else:
    print("Access denied")


                                    SECTION = D
                                    1
 def evaluate_student_performance(marks):
    
    if not (0 <= marks <= 100):
        return "Invalid marks. Please enter a value between 0 and 100."
    
    
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    else:
        grade = "C"
        
    
    status = "Pass" if marks >= 40 else "Fail"
    
    return f"Grade: {grade} | Status: {status}"


print(f"Marks 95: {evaluate_student_performance(95)}")
print(f"Marks 82: {evaluate_student_performance(82)}")
print(f"Marks 74: {evaluate_student_performance(74)}")
print(f"Marks 65: {evaluate_student_performance(65)}")
print(f"Marks 38: {evaluate_student_performance(38)}")
                                   2
 
current_time = float(input("Enter current time (0-23.99): "))
bill = float(input("Enter the bill amount: "))


store_status = ""
discount_rate = 0.0

# 1. Determine store status and calculate discount
if 9 <= current_time <= 21:
    store_status = "Store is open"
    
    
    if 18 <= current_time <= 21:
        discount_rate = 0.20
    else:
        discount_rate = 0.00
elif current_time >= 0 and current_time < 9 or current_time > 21 and current_time < 24:
    store_status = "Store is closed"
    discount_rate = 0.00
else:
    store_status = "Invalid time entered"
    discount_rate = 0.00

# 2. Calculate final bill
final_bill = bill - (bill * discount_rate)

# 3. Print the results
print("\n--- Store Summary ---")
print(f"Status: {store_status}")
print(f"Discount Applied: {discount_rate * 100}%")
print(f"Final Bill: ${final_bill:.2f}")'''
                                  