import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather",
           params= {
               "q" : "Noida",
               "appid": "60c7c2292644013f7fb8c9d434e4ec27"}             
                        )
data = response.json()
#Country = data["sys"]["country"]
#City = data["name"]
#print(Country,City)
print(data)