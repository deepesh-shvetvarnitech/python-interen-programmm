import logging



logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")


def log_process(func):

    

    def wrapper(*args, **kwargs):
        logging.info("processing started...")
        result = func(*args, **kwargs)
        logging.info("processing completed....")
        return result

    return wrapper


def shipment_generator(total_shipments):

    
    for i in range(1, total_shipments + 1):
        yield f"SHIP-{i:03d}"


@log_process  

def process_shipment(shipment_id, weight):

    
    print(f"processing {shipment_id}...")
    if weight >= 10:
        print("status checked : heavy shipment")
        return "heavy shipment"
    else:
        print("status checked : normal shipment")
        return "normal shipment"




total_shipments = 5
heavy_count = 0
normal_count = 0  




for count, shipment_id in enumerate(
    shipment_generator(total_shipments), start=1
):
    print(f"\n===================== shipment {count} =====================")
    try:
        weight_input = input(f"enter weight for {shipment_id}: ")
        weight = float(weight_input)


        
        status = process_shipment(shipment_id, weight)

        if status == "heavy shipment":
            heavy_count += 1
        else:
            normal_count += 1  
            

        print("----------------------------------------------------")
        print(f"shipment id : {shipment_id}")
        print(f"weight      : {weight} kg")
        print(f"status      : {status}")
        print("====================================================")

    except ValueError:
        logging.error("invalid input")
        print("invalid input! please enter a valid number.")

        

print("\n===================== shipment summary =====================")
print(f"total shipments : {total_shipments}")
print(f"heavy shipments : {heavy_count}")
print(f"normal shipments: {normal_count}")
print("=========================================================")






