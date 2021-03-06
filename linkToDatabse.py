from curses import endwin
import string
import time
import requests
from progress.bar import Bar




f = open("/Users/alyeldinshahin/Documents/ZakRequest.txt", "r")
links = f.readlines()

#cusName= 'sprinklr'
#authKey = 'LUrqgCXgzE'

#crimson
#Rhbvcjy1122

cusName = 'crimson'
authKey = 'Rhbvcjy1122'

failedLinks = []

#API_ENDPOINT = "http://"+cusName+":"+authKey+"@localhost:8080/"+cusName+"/youtube/main/channels"

bar = Bar('Processing', max=len(links))
print("Adding "+str(len(links))+" Record(s) To "+cusName)

for x in range(len(links)):
    #time.sleep(3)
    links[x] =links[x].strip()
    tempLink = str(links[x])
    
    if (tempLink == ""):
        continue
    #print(tempLink)
    if ("/watch/" in links[x]):
        #print("Video Number "+str(x)+ " Submitted")
        API_ENDPOINT = "http://"+cusName+":"+authKey + "@localhost:8080/"+cusName+"/youtube/main/videos"
    if("/channel/" in links[x] or "/c/" in links[x] or "/user/" in links[x]):
        #print("Channel Number "+str(x)+" Submitted")
        API_ENDPOINT = "http://"+cusName+":"+authKey + "@localhost:8080/"+cusName+"/youtube/main/channels"


    
    stringToExport = (
        '\n{\n\t\"addAll\": {\n\n\t\t"url": "'+links[x]+'"\n\t}\n}')
    #print (stringToExport)
    data = stringToExport
    r = requests.post(url=API_ENDPOINT, data=data)
    bar.next()
    #print(r.text)
    if ("failure" in r.text):
        #print("Faild at Link:\n"+str(links[x]))
        failedLinks.append(str(links[x]))

print(failedLinks)
bar.finish()



#------
