import pyowm #Importing necessary module
#documentation and Youtube guides)
from colorama import init #importing a package for Windows
from colorama import Fore, Back, Style #importing necessary packages

api_key = pyowm.OWM('26177363c268ee1d29d88a3aa230a3d8') #Getting api key
place = input('Enter place to get weather information: ') #Getting place
observation = api_key.weather_at_place(place) #Serching information
weather_info = observation.get_weather() #Highlighting weather from data
temp_info = weather_info.get_temperature('celsius')['temp'] #Getting temperature
detailed_status = weather_info.get_detailed_status() #Getting sky status
print('The temperature is ', temp_info, ' degrees Celsius', sep = '') #Outputting temperature
print('The status is ', detailed_status, sep = '') #Outputting sky status

if temp_info >= 50: #Making some checks like in examples below
    print(Back.RED, Fore.WHITE, 'It\'s very hot... Wear a T-shirt and shorts. Don\'t forget about sunscreen!', sep = '')
    #Output the recommendations
elif temp_info >= 30 and temp_info <= 50: #Two conditions using and operator
    print(Back.YELLOW, Fore.BLACK, 'It\'s summer! Wear as usually: a T-shirt and shorts!', sep = '')
    #Same for other outputs
elif temp_info >= 10 and temp_info <= 30:
    print(Back.GREEN, Fore.BLACK, 'Wear pants and a jacket!', sep = '')
elif temp_info >= -10 and temp_info <= 10:
    print(Back.CYAN, Fore.BLACK, 'It\'s not too cold, but you should wear coveralls and warm jacket!', sep = '')
elif temp_info >= -30 and temp_info <= -10:
    print(Back.BLUE, Fore.WHITE, 'Wear a jacket from Norway and warm coveralls... Ah, underpants!', sep = '')
elif temp_info <= 50:
    print(Back.MAGENTA, Fore.WHITE, 'Welcome to Antarctica! Put on everything warm! Hello to penguins!', sep = '')
else:
    raise ValueError('Incorrect value entered. Try again.') #Error raising
