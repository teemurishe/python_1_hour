from colorama import init #importing a package for Windows
from colorama import Fore, Back, Style #importing necessary packages
init() #command for Windows

print(Back.CYAN) #back for operation input
print(Fore.BLACK) #text color for operation input
operation = input('Select the operation(+/-): ') #selecting the operation

if operation == '+' or operation == '-': #check if the operation symbol is
    #correct
    print(Back.BLUE) #back for numbers input
    print(Fore.WHITE) #text color for numbers input
    num1 = float(input('Enter first number: ')) #if yes, entering numbers
    num2 = float(input('Enter second number: ')) #second input()
    if operation == '+': #summing operations
        print(Back.GREEN, Fore.BLACK, num1 + num2, sep = '') #output coloring
    if operation == '-': #minus operations
        print(Back.GREEN, Fore.BLACK, num1 - num2, sep = '') #output coloring
else: #for incorrect inputs
    print(Back.RED) #back for error
    print(Fore.WHITE) #text color for error
    raise ValueError('Incorrect oepration selected. Please, try again.')
    #raising an error with a commentary for user
 #Congratulations! Our first simple calculator is ready! But you can improve it:
 #add more operations, or even create GUI! But now we're going to create another
 #program... Go to test.py to continue!
