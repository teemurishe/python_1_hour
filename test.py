import math #Importing a module for the example of making int numbers from float
#usage: import xxx, where xxx - the name of module(this one is pre-installed,
#some modules could be installed by using pip in bash (see official Python
#documentation and Youtube guides)
from colorama import init #Importing a package to have this module working on
#Windows (install this package with pip)
from colorama import Fore, Back, Style #Importing necessary packages from module
#syntax: from xxx import yyy, zzz, aaa - where xxx - name of module, where
#yyy, zzz, aaa - necessary parts of module (you always can import all the module
#using default import xxx, where xxx - name of module)
import pyowm #Importing a module to create a weathercast program. Install module
#using pip.
init() #also a command to have the module working on Windows

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
exp = num1 ** num2 #exponentiation numbers
mod1 = num1 % num2 #dividing with module 1
mod2 = num2 % num1 #dividing with module 2
num1 = -num1 #unary minus 1
num2 = -num2 #unary minus 2
num1 = 5.41 #for the next operation, float numbers are needed
num2 = 5.87 #now there are two float numbers
num1 = round(num1) #round() operator is used to make integer number from float
num2 = round(num2) #usage: round(x), where x - variable (float) or float number
num1 = 5.41 #returning the previous value
num2 = 5.87 #to show another example
num1 = math.floor(num1) #rounding the float number, making it less, even if
num2 = math.floor(num2) #we should make it bigger (following rounding rules)
num1 = 5.41 #returning again
num2 = 5.87 #to show another example with math
num1 = math.ceil(num1) #opppositely, now we make it less
num2 = math.ceil(num2) #ignoring the rules
pi = math.pi #using math momdule to get the pi number

choice = input('Hello world or Hi, user?: ') #if operator: preparation (user
#should enter 'world' or 'user', then this choice is recorded to the choice var)
if choice == 'world': #if usage with equality: if xxx == yyy:, where xxx -
#the variable defined before the if block, where yyy - variable, string, number,
#etc.
    print('Hello world!') #the code of the if operator is under it, there is a
    #tab (4 spaces) before each string of its code
elif choice == 'user': #elif operator is used for such situations, same usage.
    print('Hi', username + '!') #Do you remember the username var (30rd str.)?
else: #This operator doesn't have conditions, it runs only when all the
#conditions before it are False
    raise NameError('Incorrect choice! Try again, please...') #Same tabulation.
    #the raise operator is needed to show an error text to user. Usage:
    #raise xxx('blablabla'), where xxx - type of error (see Python docs), where
    #blablabla - additional text which could help user to solve the problem
#Another conditions for if: != (not equal), > (more than), < (less than),
#>= (more than or equal), <= (less than or equal)

print(Back.WHITE) #Neutral color for temp. input
print(Fore.BLACK) #White text on white back doesn'look nice. Let's use black text.
#To colour the string, we should print the parameter of colour before the string
#We need two parameters now: Fore (colour of text) and Back (colour of text
#background). Syntax: print(Xxx.YYY), where Xxx - parameter, where YYY - value.
#These are the values for each parameter:
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Remember: The parameter works for every string below it. To disable, you
#should use the RESET values for both parameters below the text where they
#aren't needed.
weather = int(input('Enter the temperature in degrees Celsius: ')) #Making a simple
#program to say user what to put on using temperture data as example of coloring
#text in console.
if weather >= 50: #making some checks like in examples below
    print(Back.RED, Fore.WHITE, 'It\'s very hot... Wear a T-shirt and shorts. Don\'t forget about sunscreen!', sep = '')
    #We can also improve the output by printing colors and text in one operator.
    #The 'sep' is a key word to set your own way to separate the parts of
    #output. For example, sep = '' deletes any separators betweeen output parts.
    #Try not to make such long strings! And here you can also see shieldig.
elif weather >= 30 and weather <= 50: #Two conditions using and operator
    print(Back.YELLOW, Fore.BLACK, 'It\'s summer! Wear as usually: a T-shirt and shorts!', sep = '')
    #Same for other outputs
elif weather >= 10 and weather <= 30:
    print(Back.GREEN, Fore.BLACK, 'Wear pants and a jacket!', sep = '')
elif weather >= -10 and weather <= 10:
    print(Back.CYAN, Fore.BLACK, 'It\'s not too cold, but you should wear coveralls and warm jacket!', sep = '')
elif weather >= -30 and weather <= -10:
    print(Back.BLUE, Fore.WHITE, 'Wear a jacket from Norway and warm coveralls... Ah, underpants!', sep = '')
elif weather <= 50:
    print(Back.MAGENTA, Fore.WHITE, 'Welcome to Antarctica! Put on everything warm! Hello to penguins!', sep = '')
else:
    raise ValueError('Incorrect value entered. Try again.') #An error raising

#Now you are ready to create a simple calculator! Go to calc.py now.

api_key = pyowm.OWM('26177363c268ee1d29d88a3aa230a3d8') #getting a special api
#key to receive information from OpenWeatherMap service. You can generate your
#own one on https://home.openweathermap.org/api_keys site after registration.

place = input('Enter place: ') #user input to get the place where the weather
#should be received from

observation = api_key.weather_at_place(place) #now the program gets user's place
weather_info = observation.get_weather() #selecting weather from all the data
temp_info = weather_info.get_temperature('celsius')['temp'] #getting temperature in degrees
#celsius
detailed_status = weather_info.get_detailed_status() #getting sky status

print(weather_info, temp_info, detailed_status, sep = '\n') #new output with
#'enters' as separators

#Now you are ready to create a weather forcast program! Go to weather.py.
