from curses import endwin
import string
import time
import requests


f = open("Documents/ZakRequest.txt", "r")
links = f.readlines()

cusName= 'crimson'
authKey = 'Rhbvcjy1122'

API_ENDPOINT = "http://"+cusName+":"+authKey+"@localhost:8080/"+cusName+"/youtube/main/channels"


for x in range(len(links)):
    time.sleep(1)
    links[x] =links[x].strip()
    stringToExport = (
        '\n{\n\t\"addAll\": {\n\n\t\t"url": "'+links[x]+'"\n\t}\n}')
    data = stringToExport
    r = requests.post(url=API_ENDPOINT, data=data)
    print(r.text)


#------
