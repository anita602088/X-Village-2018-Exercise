import requests
import json

url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5"

f = open("music_show.json","w+", encoding='utf-8-sig')

response = requests.get(url)

d = json.loads(response.text) 
a = json.dumps(d,indent=4)
f.write(a)