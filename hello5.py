
"""
Program Name : hello.py  ( print python text in the Linux. )

Description : Prints Text in terminal.

Name : NS, Jo.

Date : 2025.04.01

"""

print("Hello_Python_In_The_Ubuntu_Server")


""" Return The Result Of Two Numbers"""
print('Type type_left_num which will be plused')
type_left_num = ''
type_right_num = ''
type_left_num = input(type_left_num)
type_left_num = int(type_left_num)

print('Type type_right_num which will be plused')
type_right_num = ''
type_right_num = input(type_right_num)
type_right_num =int(type_right_num)

def addNumbers(type_left_num, type_right_num) : 
    
    sumNumbers = type_left_num + type_right_num
    
    return sumNumbers

receiveNumbers = addNumbers(type_left_num, type_right_num) 
''' Assign the result to left_var after calling function'''

print(" \n Your Total Sum Number is :  \t  ", receiveNumbers)

