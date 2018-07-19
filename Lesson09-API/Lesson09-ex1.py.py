import json
import requests

url = "https://www.metaweather.com/api/location/2306179/2018/7/18"

f = open("weather.json", "w", encoding='utf-8-sig')
res = requests.get(url)
d = json.loads(res.text) 
a = json.dumps(d,indent=4)
f.write(a)

with open("weather.json","r", encoding='utf-8-sig') as f:
        x = json.load(f)
        for i in range(len(x)):
            print("Taipei:"+str(x[i]["applicable_date"])+ " / Weather state:"+str(x[i]["weather_state_name"])+" / Temp:"+ str(x[i]["the_temp"])+"\n")

