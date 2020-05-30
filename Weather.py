import requests

city = input("Enter your city: ")

url= f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid='

res= requests.get(url)

data= res.json()

temperature = data['main']['temp']

print(f'Temperature in Kelvin = {temperature}')