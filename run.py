import requests
city = input("City : ")
key = "9656046022b784a4ee34bd710a357f3e"
#city example = kolkata delhi mumbai bangalore
url = "https://api.openweathermap.org/data/2.5/forecast?q=" + city + "&appid=" + key
r = requests.get(url)


import json
weather_data = json.loads(r.text)
#print(weather_data)
#latest_data = weather_data.list[0]
latest_data = (weather_data["list"][0]["main"])
print("Temperature : " + str(latest_data["temp"]))
print("Humidity : " + str(latest_data["humidity"]))
print("Pressure : " + str(latest_data["pressure"]))
