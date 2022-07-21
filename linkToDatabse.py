from curses import endwin
import string
import time
import requests


f = open("/Users/alyeldinshahin/Documents/ZakRequest.txt", "r")
links = f.readlines()

cusName= 'sprinklr'
authKey = 'LUrqgCXgzE'

API_ENDPOINT = "http://"+cusName+":"+authKey+"@localhost:8080/"+cusName+"/youtube/main/channels"


for x in range(len(links)):
    time.sleep(1)
    links[x] =links[x].strip()
    tempLink = str(links[x])
    if ("watch" in links[x]):
        print("Video Number "+x+ " Submitted")
        API_ENDPOINT = "http://"+cusName+":"+authKey + "@localhost:8080/"+cusName+"/youtube/main/videos"
    if("channel" in links[x]):
        print("Channel Number "+x+" Submitted")
        API_ENDPOINT = "http://"+cusName+":"+authKey + "@localhost:8080/"+cusName+"/youtube/main/channels"


    
    stringToExport = (
        '\n{\n\t\"addAll\": {\n\n\t\t"url": "'+links[x]+'"\n\t}\n}')
    #print (stringToExport)
    data = stringToExport
    r = requests.post(url=API_ENDPOINT, data=data)
    print(r.text)


#------
