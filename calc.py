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

#To continue, you should open terminal (command line in Windows) and enter
#'pip install colorama' ('pip3 install colorama' for linux). If you have
#an error on linux, enter 'sudo apt install python3-pip' (deb-based systems like
#Ubuntu). Error on Windows? Re-install Python and tick the 'Add Python to PATH'
#phrse on the first step of installation.
