import requests
import emoji

city = input("Enter your city: ")

fahren= f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c42dd798a4d6392b9c32fdf90cb431c8&units=imperial'
celcius= f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=c42dd798a4d6392b9c32fdf90cb431c8&units=metric'

def request(url):
    res= requests.get(url)
    data= res.json()
    temperature = data['main']['temp']
    return temperature

try:
    res = requests.get(celcius)
    data= res.json()
    f = data['weather'][0]['main']        
except :
    print('Invalid City Name')
    exit()

print("Weather:")
if f == "Clear":
    print(emoji.emojize(":sun:"))
elif f == "Haze":
    print(emoji.emojize(":cloud:"))
elif f == "Rain":
    print(emoji.emojize(":umbrella:"))
elif f == "Clouds":
    print(emoji.emojize(":cloud:"))
elif f == "Snow":
    print(emoji.emojize(":snowflake:"))
elif f == "Thunder":
    print(emoji.emojize(":zap:"))

print(f'Temperature in Kelvin = {request(celcius)+273}')
print(f'Temperature in Fahrenheight = {request(fahren)}')
print(f'Temperature in Celcius = {request(celcius)}')