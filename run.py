#If u want to create your own weather app, you can reffer to this url = "https://openweathermap.org/api"
#key is the appid by which the data is fetched from the database of the api
import requests
city = input("City : ")
key = "9656046022b784a4ee34bd710a357f3e"
#city example = kolkata delhi mumbai bangalore
url = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + key
r = requests.get(url)


import json
weather_data = json.loads(r.text)
#print(weather_data)
#the above line prints the json format(full data)
#latest_data = weather_data.list[0]
latest_data = (weather_data["list"][0]["main"])
print("Temperature : " + str(latest_data["temp"]))
print("Humidity : " + str(latest_data["humidity"]))
print("Pressure : " + str(latest_data["pressure"]))
#one can add more attributies to it, just follow the json format and add more attributies to it
