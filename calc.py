operation = input('Select the operation(+/-): ') #selecting the operation

if operation == '+' or operation == '-': #check if the operation symbol is
    #correct
    num1 = float(input('Enter first number: ')) #if yes, entering numbers
    num2 = float(input('Enter second number: ')) #second input()
    if operation == '+': #summing operations
        print(num1 + num2)
    if operation == '-': #minus operations
        print(num1 - num2)
