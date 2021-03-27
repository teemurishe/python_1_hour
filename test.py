number = 5 #integer (int)
fnumber = 5.5 #float (float)
name = 'timur' #string (str)
status = True #boolean (bool)
status2 = False #another bool

print('test output') #string output
print(14) #integer output
print(True) #boolean output
print(28.6) #float output

print('It\'s so dangerous') #shielding

print('the best language in the world is\nPYTHON!!!') #writing on new string

print('the best language in the world is') #another way
print('PYTHON!!!')

age = 14
print('The root user on this PC is ' + name) #summing strings (concatenation)
print('The age of this user is ' + str(age) + ' years') #concatenation of
#different types of data (just make all the variables and other data
#string-typed using 'str(x)', where x - variable name or another data')

username = input('Enter your name: ') #input() using: var = input('xxx')
#where var - any variable (str default), where xxx - text for user
user_age = int(input('Enter your age: ')) # input() usage with int() to get
#an integer-typed variable
print('Hello, ' + username + '!') #just an example of using input() in simple
print('Your age is ' + str(user_age) + '. Wow!') #welcome program

num1 = 8 #math operations; first number
num2 = 4 #second number
sum = num1 + num2 #sum of numbers
dif1 = num1 - num2 #first difference of numbers
dif2 = num2 - num1 #second difference of numbers
mult = num1 * num2 #multiplying numbers
quot1 = num1 / num2 #quotient 1 (dividing)
quot2 = num2 / num1 #quotient 2 (dividing)
