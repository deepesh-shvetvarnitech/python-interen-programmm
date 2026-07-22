#                                                 Question= 1
a = 'GFG'  
b = "GeeksForGeeks"  
print(a)
print(b)
'''
GFG
GeeksForGeeks'''
#                                                 Question=2
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)
'''
I am Learning
Python String on GeeksforGeeks
I'm a 
Geek'''
#                                                  Question=3
s = "ABCDEF"
print(s[0])   
print(s[4])
'''
A
E'''
#                                                Question=4
s = "ABCDEF"
print(s[-3])  
print(s[-5])
'''
D
B'''
#                                                   Question= 5

s = "ABCDEF"
print(s[1:4])    
print(s[:3])     
print(s[3:])    
print(s[::-1])

#                                                   Question=6
s = "ABCDEF"
for char in s:
    print(char)
'''
A
B
C
D
E
F'''
#                                                    Question=7
s = "aBCDEF"
s = "A" + s[1:]  
print(s)
'''
abcdef'''
#                                                     Question=8
s = "aBCDEF"
s = "A" + s[1:]  
print(s)
'''
   ABCDEF'''


#                                                  Question=9                               
s = "ABC"
del s

#                                                     Question=10


s = "ABCD EF"
s1 = "H" + s[1:]                  
s2 = s.replace("ABC", "abc")  

print(s1)
print(s2)
'''
Output
HBCD EF
abcD EF
'''


#                                                 Question=11


s = "GeeksforGeeks"
print(len(s))

'''
13'''

#                                                     Question=12




s = "Hello World"
print(s.upper())
print(s.lower())
'''
Output
HELLO WORLD
hello world'''

#                                                Question=13



s = "   ABC   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))
'''
Output
ABC
Python is awesome'''




#                                                  Question=n


s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)
'''
Output
Hello World'''


#                                                       Question=15


s = "Hello "
print(s * 3)
'''
Output
Hello Hello Hello 
Formatting Strings'''



#                                                  Question=16

name = "Jake"
age = 22
print(f"Name: {name}, Age: {age}")
'''
Output
Name: Jake, Age: 22'''



#                                                     question= 17

s = "My name is {} and I am {} years old.".format( "Emily", 22)
print(s)
'''
Output
My name is Emil'''


#                                                      Question=18

s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)

'''
True
Fals'''


