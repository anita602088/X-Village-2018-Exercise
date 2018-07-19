import requests
import json

with open("music_show.txt","w+", encoding='utf-8-sig') as g:
    with open("music_show.json","r", encoding='utf-8-sig') as f:
        x = json.load(f)
        for i in range(len(x)):
            g.write(str(x[i]['title'])+":"+str(x[i]["startDate"])+ "~"+ str(x[i]["endDate"])+"\n")



