#                                                 #Question =1
file_name = 'example.txt'
mode = 'r'


try:
    with open(file_name, mode) as file:

        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    '''
    This is the content of the example file.
                                                 Question =2'''
with open('example.txt', 'r') as file:
    content = file.read()
    print("Read Mode:", content)


with open('new_file.txt', 'w') as file:
    file.write("This is a new file created in write mode.")


with open('example.txt', 'a') as file:
    file.write("\nThis line is appended in append mode.")


with open('binary_file.bin', 'wb') as file:
    file.write(b'\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64')


try:
    with open('new_file.txt', 'x') as file:
        file.write("This is an exclusive creation example.")
except FileExistsError:
    print("File 'new_file.txt' already exists.")
    '''
    Read Mode: This is the content of the example file.
File 'new_file.txt' already exists.
                                                   Question =3'''
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:", content)
    '''
    File Content: This is the content of the example file.'''
    #                                              Question =4
with open('text_file.txt', 'r') as text_file:
    content = text_file.read()
    print("Text File Content:", content)


with open('binary_file.bin', 'rb') as binary_file:
    content = binary_file.read()
    print("Binary File Content:", content)
    '''
    with open('binary_file.bin', 'rb') as binary_file:
    content = binary_file.read()
    print("Binary File Content:", content)'''
#                                                    Question =5
with open('example.txt', 'r') as file:
    
    content = file.read()
    print("File Content:", content)  

    '''
    File Content: This is the content of the example file.

                                                       Question =6'''
with open('example.txt', 'r') as file:
    
    content_part1 = file.read(20)
    print("Content Part 1:", content_part1)

    
    current_position = file.tell()
    print("Current File Pointer Position:", current_position)

    
    file.seek(10)

    
    content_part2 = file.read(10)
    print("Content Part 2:", content_part2) 
'''
Content Part 1: This is the content 
Current File Pointer Position: 20
Content Part 2: the cont
                                                       Question = 7'''
with open('example.txt', 'r') as file:
    
    content_part = file.read(15)
    print("Read Content:", content_part)

    '''
    Read Content: This is the con
                                                        Questioon = 8'''
with open('example.txt', 'r') as file:
    
    line1 = file.readline()
    print("Line 1:", line1)

    
    line2 = file.readline()
    print("Line 2:", line2)         
'''
Line 1: This is the first line.
Line 2: This is the second line.
                                                       Question =9'''
with open('example.txt', 'r') as file:

    for line in file:
        print("Line:", line.strip())

'''
Line: This is the first line.
Line: This is the second line.
Line: This is the third line.
'''
#                                                       Question =10
with open('new_file.txt', 'w') as file:
    # Write content to the file
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")


with open('new_file.txt', 'r') as read_file:
    content = read_file.read()
    print("File Content:")
    print(content)        
'''
File Content:
This is the first line.
This is the second line.
This is the third line'''
#                                                     Question = 11
with open('write_example.txt', 'w') as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

with open('writelines_example.txt', 'w') as file:
    lines = ["This is the first line.", "This is the second line.", "This is the third line."]
    file.writelines(line + '\n' for line in lines)
'''
Contents of 'write_example.txt':
This is the first line.
This is the second line.
This is the third line.

Contents of 'writelines_example.txt':
This is the first line.
This is the second line.
This is the third line.''' 
#                                                     Question =12
with open('existing_file.txt', 'a') as file:
    
    file.write("This is new content appended to the file.\n")


with open('existing_file.txt', 'r') as read_file:
    content = read_file.read()
    print("Updated File Content:")
    print(content)       

'''
Updated File Content:
This is the existing content of the file.
This is new content appended to the file.'''

#                                                   Question =13
with open('example.txt', 'r') as file:
    
    content_part1 = file.read(10)
    print("Content Part 1:", content_part1)

    
    file.seek(15)
    
    content_part2 = file.read(5)
    print("Content Part 2:", content_part2)        
    '''
    Content Part 1: This is th
Content Part 2: e first
                                                    Questiion = 14'''
with open('example.txt', 'r') as file:
    
    content_part1 = file.read(15)
    print("Content Part 1:", content_part1)

    
    current_position = file.tell()
    print("Current File Pointer Position:", current_position)

    
    content_part2 = file.read(10)
    print("Content Part 2:", content_part2) 

    '''
    Content Part 1: This is the con
Current File Pointer Position: 15
Content Part 2: tent of the
                                                    Question =15'''
    import os


file_path = 'example.txt'


if os.path.exists(file_path):

    with open(file_path, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)
else:
    print(f"The file '{file_path}' does not exist.")
    #                                             Question =16
class CustomFileContextManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        
        self.file = open(self.file_path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        
        if self.file:
            self.file.close()


file_path = 'example.txt'
mode = 'r'


with CustomFileContextManager(file_path, mode) as file:
    
    content = file.read()
    print("File Content:")
    #                                        Question = 17
    file_path = 'nonexistent_file.txt'


try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
file_path = 'read-only-file.txt'


try:
    with open(file_path, 'w') as file:
        file.write("This is a write operation.")
except PermissionError:
    print(f"Permission error: Unable to write to the file '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    #                                       Question =18
    file_path = 'flush_example.txt'


with open(file_path, 'w') as file:
    
    file.write("This is some data without flushing.")

    
    file.flush()

    
    file.write("This data is written after flushing.")


with open(file_path, 'r') as read_file:
    content = read_file.read()
    print("File Content:")
    print(content)
    '''
    File Content:
This is some data without flushing.This data is written after flushing.
                                          Question = 19'''
    file_path = 'truncate_example.txt'


with open(file_path, 'w') as file:
    
    file.write("This is some initial data.")


with open(file_path, 'r') as read_file:
    content_before = read_file.read()
    print("File Content Before Truncating:")
    print(content_before)


with open(file_path, 'r+') as file:
    
    file.seek(10)

    file.truncate()


with open(file_path, 'r') as read_file:
    content_after = read_file.read()
    print("File Content After Truncating:")
    print(content_after)

    '''
    File Content Before Truncating:
This is some initial data.
File Content After Truncating:
This is some'''
#                                              Question =20
import csv


data_to_write = [
    ['Name', 'Age', 'City'],
    ['Alice', 28, 'New York'],
    ['Bob', 35, 'San Francisco'],
    ['Charlie', 22, 'Los Angeles']
]


csv_file_path = 'example.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_to_write)


with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    
    header = next(csv_reader, None)
    if header:
        print("CSV Header:", header)
    
    
    print("CSV Content:")
    for row in csv_reader:
        print(row)
''''
CSV Header: ['Name', 'Age', 'City']
CSV Content:
['Alice', '28', 'New York']
['Bob', '35', 'San Francisco']
['Charlie', '22', 'Los Angeles']'''
#                                            Question =21
import os


file_path = 'example_directory/example_file.txt'


directory_name = os.path.dirname(file_path)
print("Directory Name:", directory_name)


base_name = os.path.basename(file_path)
print("Base Name:", base_name)


new_path = os.path.join('parent_directory', 'child_directory', 'new_file.txt')
print("New Path:", new_path)


file_exists = os.path.exists(file_path)

print("File Exists:", file_exists)

'''
Directory Name: example_directory
Base Name: example_file.txt
New Path: parent_directory/child_directory/new_file.txt
File Exists: False'''

#                                                  Question =22
import json


data_to_write = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}


json_file_path = 'example.json'
with open(json_file_path, 'w') as json_file:
    json.dump(data_to_write, json_file, indent=2)


with open(json_file_path, 'r') as json_file:
    data_read = json.load(json_file)
    print("JSON Content Read:")
    print(data_read)
    '''
    JSON Content Read:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
'''
#                                           Question =23
import pickle


data_to_serialize = {
    'name': 'Alice',
    'age': 25,
    'city': 'Wonderland'
}


pickle_file_path = 'example.pickle'
with open(pickle_file_path, 'wb') as pickle_file:
    pickle.dump(data_to_serialize, pickle_file)


with open(pickle_file_path, 'rb') as pickle_file:
    data_deserialized = pickle.load(pickle_file)
    print("Deserialized Data:")
    print(data_deserialized)
    '''
    Deserialized Data:
{'name': 'Alice', 'age': 25, 'city': 'Wonderland'}
                                         Question =24'''
    binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'  


binary_file_path = 'example_binary_file.bin'
with open(binary_file_path, 'wb') as binary_file:
    binary_file.write(binary_data)


with open(binary_file_path, 'rb') as binary_file:
    read_binary_data = binary_file.read()
    print("Read Binary Data:")
    print(read_binary_data)
    '''
    Read Binary Data:
b'Hello World'''
#                                      Question =25
text_data = "Café au Lait"


file_path = 'example_text_file.txt'
with open(file_path, 'w', encoding='utf-8') as text_file:
    text_file.write(text_data)


with open(file_path, 'r', encoding='utf-8') as text_file:
    read_text_data = text_file.read()
    print("Read Text Data:")
    print(read_text_data)

    '''
    Read Text Data:
Café au Lait'''