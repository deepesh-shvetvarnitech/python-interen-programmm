'''     SECTION = A 
1
ANS = ADDTION
2
ANS = REMINDER OF A/B 
3
ANS = A raised to the power  B 
4
ANS = A=+1
5
ANS = ARITHEMATIC OPERATION
6
ANS = TRUE IF x and y have the same Value
7
ans = True
8
ans = True
9
ans = true 
10 
ans = True
11
ans = True 
12 
ans = True
13
ans = the price including tax 
14
ans = 3
15
 ans = True
16 
ans = comparision and conditional expression
17
ans = Membership
18
ans = age elgibity check
19
ans = arithematic and comparission
20
ans = wheather a and b have same object
  
                                                  SECTION = B 
1_
 (a)
ANS = +_*%///
(B)
ANS = + (Addition): 5 + 2 evaluates to 7.Real-World: total = price + tax (calculating final bill).
(C)
ANS= 5==5-True
5!=3:TRUE,5<3:FALSE, 5>3 : TRUE, 5<=3:FALSE , 5>=3: True
(d)
ANS : AGE = 20
HAS ITS ID = True
IF AGE >18 AND HAS ITS ID  :
    PRINT("ACCESS GRANTED")
ELSE:
     PRINT("ACCESSS DENIED")
3
(a)
ANS= X=10, X+=5, X-=2:X=X-2 , X*=2 : X=X*2 , X/=2 : X=X/2
(B)
ANS = TOTAL = 00.0
ITEM_PRICES = [10.9,3.4,8.6]
FOR PRICE IN ITEM PRICES :
    TOTAL += ITEM_PRICES
PRINT(f"total bill " , {total}
      )
(c)
ans = it reduces the redundancy
4
(a)
 ans = 
== checks that both  the varian=vle RE EQUAL
IS CHECK THAT BOTH OBJECT ARE IN IN SAME Memor
A=B=10 ,BOTH A==B A IS B EVALUTE TO True
(B)
PRINT(2,IN)
PRINT("APPLE" IN ("APPLE" , "BANANA"))
PRINT(5 IN {1,2,4})
(C)
ALLOWED_ROLES = {"ADMINN", "MANAGER","EDITOR"}
USER_ROLES = "GUEST"
IF USER_ROLES IN USER_ROLES:
 PRINT("ACCESS GRANTED")
ELSE :
 PRINT("ACCESS DENIED"
       )

price = 19.99 
quantity = 3
sub_total = price * quantity
tax_rate = 0.12 
total = sub_total * (1 + tax_rate)
print (f"subtotal,{sub_total}")
                                                  3(b)
n  = 17
if n%5==0:
        print("f{n} is even")
else:
        print("f {n} is odd")
if n%5==0 and n%3==0 :
        print("f {n}is divisible by both 5 and 3")
else:
        print("f {n}is not divisible by both 5 and 3")    
                                                   3(c)
age = 20
has_license = True


can_vote = age >= 18
can_drive = age >= 18 and has_license


print(f"Can vote: {can_vote}")
print(f"Can drive: {can_drive}")

if can_vote and can_drive:
    print("The person is fully eligible to both vote and drive.")
elif can_vote or can_drive:
    print("The person meets partial eligibility requirements.")            
                                                3(d)
    income = 50000.0
expenses = 38000.0


savings = income - expenses
is_over_budget = expenses > income


print(f"Total calculated savings: ${savings:.2f}")

if is_over_budget:
    print("Warning: Expenses have exceeded income allocations.")
else:
    print("Financial status stable: Expenditures remain within targeted limits.")
                                           3(e)
    cart = ["laptop", "mouse", "keyboard"]


if "laptop" in cart:
    print("Item verification: laptop found in your current cart.")
else:
    print("Item missing: laptop not found.")

if "monitor" in cart:
    print("Item verification: monitor found in your current cart.")
else:
    print("Notice: monitor not in cart.")
                                          4(f)
    score = 85
attendance_percentage = 92


has_passed = score >= 50 and attendance_percentage >= 75
needs_improvement = score < 50 or attendance_percentage < 75

print(f"Academic parsing criteria status - Passed: {has_passed}")

if has_passed:
    if score >= 85:
        print("Final Classification: Passed with distinguished Honours.")
    else:
        print("Final Classification: Standard Pass clearance.")
elif needs_improvement:
    print("Final Classification: Academic remediation required.")
                                         4(g)
    marks = 78


percentage = (marks / 100) * 100


if marks >= 90:
    grade = "A"
elif marks >= 70:
    grade = "B"
else:
    grade = "C"


print(f"Percentage Calculated: {percentage}%")
print(f"Assigned Grade Result: {grade}")
                                        SECTION 4
A 
ANS = marks1 = 85.0
marks2 = 72.5
marks3 = 91.0


total = marks1 + marks2 + marks3
average = total / 3


is_passed = average >= 40
if average >= 90:
    grade = "A"
elif average >= 70:
    grade = "B"
else:
    grade = "C"

# 5. Output student performance metrics
print(f"Total Marks Achieved: {total:.2f}")
print(f"Calculated Average:   {average:.2f}%")
print(f"Passing Status:       {is_passed}")
print(f"Assigned Grade:       {grade}") 

B                                         
sub_total = 1250.00      
discount_rate = 0.10     
tax_rate = 0.12        
shipping_fee = 45.00     
coupon_value = 25.00     


discounted = sub_total * (1 - discount_rate)
tax_amount = discounted * tax_rate
final_total = discounted + tax_amount


final_total += shipping_fee   
final_total -= coupon_value 


print(f"--- INVOICE SUMMARY ---")
print(f"Cart Subtotal:  ${sub_total:.2f}")
print(f"After Discount: ${discounted:.2f}")
print(f"Tax Component:  ${tax_amount:.2f}")
print(f"Shipping Fee:   +${shipping_fee:.2f}")
print(f"Coupon Applied: -${coupon_value:.2f}")
print(f"-----------------------")
print(f"Final Total Due: ${final_total:.2f}")'''