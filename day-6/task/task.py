
def calculate_bill(quantity,price_per_item):
    total_price = quantity *price_per_item
    return total_price
product_list =[]
final_bill = 0
for i in range(1,6):
    print("\n==================product======================")
product_name = input("enter the product name")
quantity = int(input("enter the quantity"))
price_per_item =   int(input("enter the price of item"))

product_list.append(product_name)
total_price = calculate_bill(quantity,price_per_item)
if total_price>=10000:
    discount = "Applied"
else:
    discount ="not applied"
final_bill = final_bill + total_price
print("========================================================") 
print(f"product name :{product_name}")
print(f"quantity : {quantity}")    
print(f"peice of item : {price_per_item}")
print(f"total priee :  {total_price}")
print(f"discount : {discount}")
print("========================================================")


print("====================================SHOPPING CART SUMMARY==========================")
print()
print(f"list of product :{product_name}")
print(f"ttotal price :{total_price}")
print(f"final bil {final_bill}")
print()
print("====================================================================================")
