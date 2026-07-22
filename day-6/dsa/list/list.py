#                                        Question=1
my_list = [1, 2, 3, 'four', 5.0]


print(my_list[0])  
print(my_list[3])  


my_list[1] = 'two'
print(my_list)  


my_list.append(6)
print(my_list)  


my_list.remove('four')
print(my_list)  


subset = my_list[1:4]
print(subset)
'''1
four
[1, 'two', 3, 'four', 5.0]
[1, 'two', 3, 'four', 5.0, 6]
[1, 'two', 3, 5.0, 6]
['two', 3, 5.0]
                                              question=2'''
empty_list = []


print(type(empty_list))  
print(empty_list) 
'''
 <class 'list'>
[] 
                                                 
                                                 
                                              question =3'''
my_list = [1, 2, 3, 'four', 5.0]


my_list[1] = 'two'
print(my_list)

my_tuple = (1, 2, 3, 'four', 5.0)
'''
[1, 'two', 3, 'four', 5.0]
                                             question=4'''
my_list = [1, 2, 3, 'four', 5.0]


first_element = my_list[0]
third_element = my_list[2]
last_element = my_list[-1]

print(first_element)  
print(third_element)  
print(last_element)   


second_to_last_element = my_list[-2]
print(second_to_last_element) 

'''
1
3
5.0
four
                                              Question =5'''
my_list = [10, 20, 30, 40, 50]


third_element = my_list[2]
print(third_element)  


third_element_negative = my_list[-3]
print(third_element_negative)
'''
30
30
                                                Question = 6'''
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


sublist = my_list[2:5]
print(sublist)  


every_second = my_list[::2]
print(every_second)  


reversed_list = my_list[::-1]
print(reversed_list)  
'''
[2, 3, 4]
[0, 2, 4, 6, 8]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
                                                Question=7'''
my_list = [1, 2, 3]


my_list.append(4)


print(my_list) 
'''
[1, 2, 3, 4]
                                               Question=8'''
my_list = [1, 2, 3]


my_list.append(4)
print(my_list)  


my_list.append([5, 6])
print(my_list)  

my_list = [1, 2, 3]


my_list.extend([4, 5, 6])
print(my_list)  


my_list.extend((7, 8, 9))
print(my_list)  
'''
[1, 2, 3, 4]
[1, 2, 3, 4, [5, 6]]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
                                                Question=9'''
my_list = [1, 2, 3, 5]


my_list.insert(3, 4)


print(my_list)

list1 = [1, 2, 3]
list2 = [4, 5, 6]


list1.insert(1, list2)


print(list1)  
'''
[1, 2, 3, 4, 5]
[1, [4, 5, 6], 2, 3]
                                                Question=10'''
my_list = [1, 2, 3, 2, 4, 5]


my_list.remove(2)


print(my_list)

my_list = [1, 2, 3, 4, 5]


removed_element = my_list.pop(2)


print(my_list)
print(removed_element)

'''
[1, 3, 2, 4, 5]
[1, 2, 4, 5]
3
                                                Question =11'''
my_list = [1, 2, 3, 4, 5]


element_present = 3 in my_list
print(element_present)  


element_not_present = 6 not in my_list
print(element_not_present)
'''
True
True
                                                Question =12'''
original_list = [1, 2, 3, 4, 5]


element_to_check = 3
element_present = element_to_check in original_list


print(element_present) 
'''
True'''
original_list = [1, 2, 3, 4, 5]


squares_list = [x**2 for x in original_list]


print(squares_list)

'''[1, 4, 9, 16, 25]
                                               Question= 13'''
my_list = [1, 2, 3, 2, 4, 2, 5]


count_of_2 = my_list.count(2)


print(count_of_2)  

'''
3
                                               Question=14'''
my_list = [1, 2, 3, 4, 5]


my_list.reverse()


print(my_list)

'''
[5, 4, 3, 2, 1]
                                              Question=14'''
numbers = [4, 2, 8, 1, 5]


numbers.sort()


print(numbers)

numbers = [4, 2, 8, 1, 5]


numbers.sort(reverse=True)


print(numbers) 

'''
[1, 2, 4, 5, 8]
[8, 5, 4, 2, 1]


                                           Question =15'''
import copy


original_list = [1, [2, 3], [4, 5]]


shallow_copy = copy.copy(original_list)


shallow_copy[1][0] = 999


print(original_list)  
print(shallow_copy)

import copy


original_list = [1, [2, 3], [4, 5]]


deep_copy = copy.deepcopy(original_list)


deep_copy[1][0] = 999


print(original_list)  
print(deep_copy)

'''
[1, [999, 3], [4, 5]]
[1, [999, 3], [4, 5]]
[1, [2, 3], [4, 5]]
[1, [999, 3], [4, 5]]
                                           Question = 16'''
my_list = [1, 2, 3, 4, 5]


for element in my_list:
    
    print("Element:", element)
'''
Element: 1
Element: 2
Element: 3
Element: 4
Element: 5'''

my_list = [1, 2, 3, 4, 5]


for i in range(len(my_list)):
    
    print("Element at index", i, ":", my_list[i])
'''
Element at index 0 : 1
Element at index 1 : 2
Element at index 2 : 3
Element at index 3 : 4
Element at index 4 : 5'''    

#                                          Question =17
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]


zipped_data = zip(names, ages)


for data in zipped_data:
    print("Name:", data[0], "| Age:", data[1])
    '''
    Name: Alice | Age: 25
Name: Bob | Age: 30
Name: Charlie | Age: 22'''
#                                         Question=18
nested_list = [1, [2, 3], [4, 5, 6], 7]


print(nested_list)
'''
[1, [2, 3], [4, 5, 6], 7]
                                           Question=19
'''
numbers = [4, 2, 8, 1, 5]


numbers.sort()


print(numbers)  
# Output: [1, 2, 4, 5]
#                                          Question=20
my_list = [1, 2, 3, 4, 5]


print("Original List:", my_list)


my_list.clear()


print("List after clear():", my_list)
'''
Original List: [1, 2, 3, 4, 5]
List after clear(): []'''