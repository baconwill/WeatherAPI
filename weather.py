import requests

api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid=d5ecb8e607da6c39003234525df39306&q='
city = input("City Name: ")
url = api_adress + city

json_data = requests.get(url).json()
Weather = json_data['weather'][0]['description']
Temp = json_data['main']['temp']

Celcius = int(round((Temp - 273.15),0))
Farenheight = round((Celcius*(9/5)) + 32)


print("Forecast: " + Weather)

print("Temperature: " + str(Celcius) + " C")
print("Temperature: " + str(Farenheight) + " F")

 