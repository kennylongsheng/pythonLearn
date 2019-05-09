import requests

api_add = ("""http://api.openweathermap.org/data/2.5/weather?appid=837569d4c40bcd2c3d478257d41b4c99&q=""")

city = input("City_name: ")

url = api_add + city

data = requests.get(url).json()

def Cel(Fer):
	celc = (Fer - 273.15)
	#print(celc)
	return int(celc)

print("Weather: " +  data["weather"][0]["main"] + " (" + data["weather"][0]["description"] + ")")
print("Temperature: " + str(Cel((int)(data["main"]["temp"]))) + "  (Max: " + str(Cel((int)(data["main"]["temp_max"]))) + ", Min: " + str(Cel((int)(data["main"]["temp_min"]))) + ")" )
