import csv
reader = None
f = open("AQI.csv", "r", encoding='utf-8-sig')
reader = csv.reader(f)

listall=[]
for i in reader:
    listall.append(i)

lista = [None,200]

for line in listall[1:] :
    if int(line[2])< int(lista[1]):
        lista[1] = line[2]
        lista[0] = line[0]

print(lista[0], "空氣最好")
print("AQI是", lista[1])
