import requests

city = input("Enter your city: ")

fahren= f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid= &units=imperial'
celcius= f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid= &units=metric'

def request(url):
    res= requests.get(url)
    data= res.json()
    temperature = data['main']['temp']
    return temperature

print(f'Temperature in Kelvin = {request(celcius)+273}')
print(f'Temperature in Fahrenheight = {request(fahren)}')
print(f'Temperature in Celcius = {request(celcius)}')