final_bill=0
for i in range(1,6):
    print("\n enter the details of product")
product_name=input("enter the product name")
Quantity = int(input("enter the quantity"))
price_per_item=int(input("enter the price per item"))
total_price= Quantity * price_per_item  
final_bill = final_bill + total_price 
if total_price >=1000:
    discount = "Applied" 
    print("discount Applied")
else:
    discount = "no discount"

print("------------------------------------------")
print(f" product name {product_name}")
print(f" Quantity {Quantity}")
print(f"print price per item  {price_per_item}")
print(f" total price {total_price}")
print(f"final bill {final_bill}")
print(f"discount {discount}")

print("\n===================DROCERY BILL SUMMARY")
print("total product : 5")
print(f"final bill : RS +str{final_bill}")
print("============================================")

