from colorama import init #importing a package to have this module working on
#Windows
from colorama import Fore, Back, Style #importing necessary packages from module
#syntax: from xxx import yyy, zzz, aaa - where xxx - name of module, where
#yyy, zzz, aaa - necessary parts of module (you always can import all the module
#using default import xxx, where xxx - name of module)

operation = input('Select the operation(+/-): ') #selecting the operation

if operation == '+' or operation == '-': #check if the operation symbol is
    #correct
    num1 = float(input('Enter first number: ')) #if yes, entering numbers
    num2 = float(input('Enter second number: ')) #second input()
    if operation == '+': #summing operations
        print(num1 + num2)
    if operation == '-': #minus operations
        print(num1 - num2)
else: #for incorrect inputs
    raise ValueError('Incorrect oepration selected. Please, try again.')
    #raising an error with a commentary for user
