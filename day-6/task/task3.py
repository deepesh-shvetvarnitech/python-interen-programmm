def check_stock(quantity):
    if quantity<=10:
        return "Restock required"
    else:
        return "Sock required"
    
    inventory = []

    restore_count = 0
    highest_quantity = 0
    for i in range(1,6):
        print("\n=================================Product=======================")
        product_name = input("enter the product name")
        quantity = int(input("enter the available quantity"))
        inventary[product_name] = quantity
        status = check_stock(quantity)
        if status == "Restock required":
            restock_count = restock_count+1
        if quantity > highest_quantity:
            highest_quantity = quantity  
            highest_product = product_name
            print("===========================================================")
            print(f"product name : {product_name}")
            print(f"quatity: {quantity}") 
            print(f"Status : {status}" )
            print("===========================================================")
        total_product = len(inventory)
        stock_available = total_products-restock_count 
        print("\n========================inventory summmary==================\n")
        print("invenotry")
        print(invertory)
        print()
        print(f"total product : {total_product}")
        print(f"Restock required : {restock_count}")
        print(f"Stock Available : {stock_available}")
        print(f"Highest Stock Product : {highest_quantity}")
        print("\n===============================================================")

              