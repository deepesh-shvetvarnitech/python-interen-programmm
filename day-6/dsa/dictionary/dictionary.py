#                                            Question=1
person = {
    "Name": "John",
    "Age": 25,
    "City": "New York"
}


print("Name:", person["Name"])
print("Age:", person["Age"])
print("City:", person["City"])
'''Output:

Name: John
Age: 25
City: New York'''

#                                             Question= 2
empty_dict1 = {}
print("Empty Dictionary 1:", empty_dict1)


empty_dict2 = dict()
print("Empty Dictionary 2:", empty_dict2)
'''Output:

Empty Dictionary 1: {}
Empty Dictionary 2: {}'''

#                                             Question =3
student_info = {
    "Name": "John",
    "Age": 25,
    "City": "New York"
}


print("Name:", student_info["Name"])
print("Age:", student_info["Age"])
print("City:", student_info["City"])


student_info["Age"] = 26
student_info["Grade"] = "A"


print("Modified Dictionary:", student_info)


del student_info["City"]


print("Final Dictionary:", student_info)
'''Output:

Name: John
Age: 25
City: New York
Modified Dictionary: {'Name': 'John', 'Age': 26, 'City': 'New York', 'Grade': 'A'}
Final Dictionary: {'Name': 'John', 'Age': 26, 'Grade': 'A'}'''

#                                            Question =4
student_info = {"Name": "John", "Age": 25, "City": "New York"}


grades = [90, 85, 92, 88]


coordinates = (3, 5)


student_info["Age"] = 26


grades[1] = 87


coordinates[0] = 4

name = student_info["Name"]


grade = grades[1]


x = coordinates[0]
student_info["Grade"] = "A"


grades.append(95)


new_coordinates = coordinates + (7, 2)
''' Output:

Dictionary: {'Name': 'John', 'Age': 26, 'City': 'New York', 'Grade': 'A'}
List: [90, 87, 92, 88, 95]
Tuple: (3, 5, 7, 2)'''

#                                       Question =5
student_info = {"Name": "John", "Age": 25, "City": "New York"}


name = student_info["Name"]
age = student_info["Age"]
city = student_info["City"]


print("Name:", name)
print("Age:", age)
print("City:", city)
'''Output:

Name: John
Age: 25
City: New York'''

#                                       Question = 6
student_info = {"Name": "John", "Age": 25, "City": "New York"}


name = student_info.get("Name")
grade = student_info.get("Grade", "Not Available")


print("Name:", name)
print("Grade:", grade)
'''Output:

Name: John
Grade: Not Available'''

#                                       Question=7
student_info = {"Name": "John", "Age": 25, "City": "New York"}


student_info["Grade"] = "A"


print(student_info)
'''Output:

{'Name': 'John', 'Age': 25, 'City': 'New York', 'Grade': 'A'}'''
#                                      Qiestion =8
student_info = {"Name": "John", "Age": 25, "City": "New York"}


additional_info = {"Grade": "A", "Hobbies": ["Reading", "Coding"]}


student_info.update(additional_info)


print(student_info)
'''Output:

{'Name': 'John', 'Age': 25, 'City': 'New York', 'Grade': 'A', 'Hobbies': ['Reading',, 'Coding']}'''
#                                    Question=9
student_info = {"Name": "John", "Age": 25, "City": "New York"}


removed_value = student_info.pop("Age")


print("Updated Dictionary:", student_info)
print("Removed Value:", removed_value)
'''Output:

Updated Dictionary: {'Name': 'John', 'City': 'New York'}
Removed Value: 25  '''                     

#                                    Question =10
student_info = {"Name": "John", "Age": 25, "City": "New York"}


removed_value = student_info.pop("Age")


print("Updated Dictionary:", student_info)
print("Removed Value:", removed_value)
'''Output:

Updated Dictionary: {'Name': 'John', 'City': 'New York'}
Removed Value: 25'''
#                                    Question=11
student_info = {"Name": "John", "Age": 25, "City": "New York"}


removed_value = student_info.pop("Age")


print("Updated Dictionary:", student_info)
print("Removed Value:", removed_value)
'''Output:

Updated Dictionary: {'Name': 'John', 'City': 'New York'}
Removed Value: 25'''

#                                    Question =12
sample_dict = {'name': 'John', 'age': 25, 'city': 'New York'}


key_to_check = 'age'
if key_to_check in sample_dict:
    print(f"{key_to_check} is present in the dictionary.")
else:
    print(f"{key_to_check} is not present in the dictionary.")


key_to_check = 'gender'
value = sample_dict.get(key_to_check, 'Key not found')
print(f"{key_to_check}: {value}")
'''Output:

age is present in the dictionary.
gender: Key not found'''

#                                    Question =13
sample_dict = {'name': 'John', 'age': 25, 'city': 'New York'}


keys = sample_dict.keys()
print("Keys:", keys)


values = sample_dict.values()
print("Values:", values)


items = sample_dict.items()
print("Items:", items)
'''Output:

Keys: dict_keys(['name', 'age', 'city'])
Values: dict_values(['John', 25, 'New York'])
Items: dict_items([('name', 'John'), ('age', 25), ('city', 'New York')])'''

#                                     Question=14
sample_dict = {'name': 'John', 'age': 25, 'city': 'New York'}


print("Iterating over keys:")
for key in sample_dict:
    print("Key:", key)


print("\nIterating over values:")
for value in sample_dict.values():
    print("Value:", value)


print("\nIterating over key-value pairs:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")
'''Output:

Iterating over keys:
Key: name
Key: age
Key: city

Iterating over values:
Value: John
Value: 25
Value: New York

Iterating over key-value pairs:
name: John
age: 25
city: New York'''

#                                              Question=15
sample_dict = {'name': 'John', 'age': 25, 'city': 'New York'}


removed_item = sample_dict.pop('age')


print(f"Removed item: {removed_item}")
print("Updated dictionary:", sample_dict)


non_existing_key = 'gender'
default_value = 'Not specified'
default_item = sample_dict.pop(non_existing_key, default_value)


print(f"\nRemoved item with default value: {default_item}")
print("Updated dictionary:", sample_dict)
'''Output:

Removed item: 25
Updated dictionary: {'name': 'John', 'city': 'New York'}

Removed item with default value: Not specified
Updated dictionary: {'name': 'John', 'city': 'New York'}'''

#                                           Question=16
sample_dict = {'name': 'John', 'age': 25, 'city': 'New York'}


print("Original dictionary:", sample_dict)


sample_dict.clear()


print("Dictionary after using clear():", sample_dict)
'''Output:

Original dictionary: {'name': 'John', 'age': 25, 'city': 'New York'}
Dictionary after using clear(): {}'''

#                                          Question =17
nested_dict = {
    'person1': {'name': 'John', 'age': 25, 'city': 'New York'},
    'person2': {'name': 'Alice', 'age': 30, 'city': 'San Francisco'}
}


print("Name of person1:", nested_dict['person1']['name'])
print("Age of person2:", nested_dict['person2']['age'])
'''Output:

Name of person1: John
Age of person2: 30'''

#                                           Question =18
original_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

shallow_copy_dict = original_dict.copy()


shallow_copy_dict['age'] = 30


print("Original Dictionary:", original_dict)
print("Shallow Copy Dictionary:", shallow_copy_dict)
'''Output:

Original Dictionary: {'name': 'John', 'age': 25, 'city': 'New York'}
Shallow Copy Dictionary: {'name': 'John', 'age': 30, 'city': 'New York'}'''

#                                          Question =19
from collections import defaultdict


default_dict = defaultdict(int)


default_dict['count'] += 1


print("Default Dictionary:", default_dict)
'''Output:

Default Dictionary: defaultdict(, {'count': 1})'''

#                                        Question= 20
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_set = {1, 2, 3, 4, 5}
'''Outputs:

Dictionary: {'name': 'John', 'age': 25, 'city': 'New York'}
Set: {1, 2, 3, 4, 5}'''