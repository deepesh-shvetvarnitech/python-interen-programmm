def check_email(email):
    email = email.lower()
    if "@" in email and email ".com" in email:
        return"Valid"
    else:
        return"not valid"
employee_list =[]
valid_email_count = 0
for i in range(1,6):
    print("\n====================employeeee=================")
    employee_name = input("enter the employee name")
    employee_email = input("enter the employee email")
    employee_list.append(employee_name)
    status_check = check_email(employee_name)
    if status_check == "valid":
        valid_email_count = valid_email_count+1
        print("\n--------------------------------")
        print(f"employee name : {employee_name}")
        print(f"employee email : {employee_email}")
        print(f"status : {status_check}")
        print("---------------------------------")
total_employee = len(employee_list)
Invaild_email_count = total_employee-valid_email_count

print("\n========================employee summary=========================")
print()
print(f"Total empoyee : {total_employee}") 
print(f"Vaild email : {valid_email_count}")  
print(f"Invaild email : {Invaild_email_count}")
print("\============================================================================")                     