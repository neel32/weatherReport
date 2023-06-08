import requests
import json
import os
import pyttsx3


engine = pyttsx3.init()

city = input("Enter the name of the city : \n")

url = f"https://api.weatherapi.com/v1/current.json?key=4fb0d79149a344a3bcf74910230806&q={city}"

r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

engine.say(f"say 'The current weather in {city} is {w} degree'")
engine.runAndWait()
# os.system(f"say 'The current weather in {city} is {w} degree'")