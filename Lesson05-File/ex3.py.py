import json

with open('TransService.json',"r", encoding = 'utf8') as f:
    trans = json.load(f)
    print(trans)
    print(json.dumps(trans, indent=4))