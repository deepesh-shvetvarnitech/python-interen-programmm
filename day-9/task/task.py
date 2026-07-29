import logging
loigging.basicConfig()
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
class  BankAccount:
    def __init__(self,customer_name,balance):
       self.customer_name = customer_name
       self.balance = balance
    def withdraw(self,amount):
        if self.balance >= amount:     
           self.balance -= amount
           return "withdraw successsfull"      
        else:
           return "insuficient balance"
successfull_withdraw = 0
high_balance_customer = 0
total_customer = 5 
for customer in range(1,total_customer+1):
   print(f"==================customer{customer}==========")
try:
      customer_name = input("enter coustomer name :")
      balance = float(input("enter current balance :" ))
      amount = float(input("enter your withdraw amount"))
      original_balance = balance
      account = BankAccount(customer_name,balance)
      loigging_info("customer created")
      status = account.withdraw(amount)
      if status=="withdraw successsfull":
         successfull_withdraw +=1
         loigging.info("withdraw successfull")
      else:
         logging.warning("insufficient balance")
      if account.balance >= 500:
         high_balance_customer += 1

      print(f"========================================")
      print(f" customer name : {customer_name}" ) 
      print(f" balance : {original_balance}" )       
      print(f" balance : {original_balance}" )       
            
      print(f"withdraw : {amount} ")
      print(f"status : {status}")
      print(f" remaining : {account.balance}")
      print("==========================================")
except ValueError:
    logging.error("invalid input")
    print("invalid input : please enter a number")
    continue
failed_withdraw = total_customer - successfull_withdraw
print(f"==========================bank summary=========")
print(f" total coustomer : {total_customer}")
print(f"successfull withdraw : {successfull_withdraw}")
print(f" failed withdraw  : {failed_withdraw}")
print("coustomer with balance >= 500 : {high_balance_coustomer}")
print("================================================")
assert BankAccount("Rahul " ,500).withdraw(200)=="withdraw successsfull"
assert BankAccount("Aman " ,300).withdraw(300)=="insufficient balance"
print(" all the test cases pass succes fully")


                                    
