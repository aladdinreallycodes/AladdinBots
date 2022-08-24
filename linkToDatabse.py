#from curses import endwin
from re import template
#from curses import endwin
import string
import time
import requests
from progress.bar import Bar



def mainProg(cusName , authKey):

    f = open("ZakRequest.txt", 'r',
            encoding='UTF-8')

    links = f.readlines()



    failedLinks = []

    #API_ENDPOINT = "http://"+cusName+":"+authKey+"@localhost:8080/"+cusName+"/youtube/main/channels"

    bar = Bar('Processing', max=len(links))
    print("Adding "+str(len(links))+" Record(s) To "+cusName)

    for x in range(len(links)):
        #time.sleep(3)
        links[x] =links[x].strip()
        tempLink = str(links[x])
        #print(tempLink[0])

        if (tempLink == ""):
            continue
        if (tempLink[0] != 'h'):
            #print("Link Dont work")
            #print (tempLink)
            links[x] = "http://"+tempLink
            #print(tempLink)
        #print(tempLink)


        if ("/watch?" in links[x]):
            #print("Video Number "+str(x)+ " Submitted")
            API_ENDPOINT = "http://"+cusName+":"+authKey + "@localhost:8080/"+cusName+"/youtube/main/videos"
        elif("/channel/" in links[x] or "/c/" in links[x] or "/user/" in links[x]):
            #print("Channel Number "+str(x)+" Submitted")
            API_ENDPOINT = "http://"+cusName+":"+authKey + "@localhost:8080/"+cusName+"/youtube/main/channels"
        else:
            API_ENDPOINT = "http://"+cusName+":"+authKey + "@localhost:8080/"+cusName+"/youtube/main/channels"





        
        stringToExport = (
            '\n{\n\t\"addAll\": {\n\n\t\t"url": "'+links[x]+'"\n\t}\n}')
        data = stringToExport
        r = requests.post(url=API_ENDPOINT, data=data)
        bar.next()
        #print(r.text)          <--Uncomment this line if you want to see the results of every api call
        if ("failure" in r.text):
            failedLinks.append(str(links[x]))

    print(failedLinks)
    bar.finish()


if __name__ == "__main__":
    comp = input("\nChoose company to add links to:\n1)Crimson\n2)Sprinklr\n")
    comp = int(comp)
    
    if comp == 1:
        
        cusName = 'crimson'
        authKey = 'Rhbvcjy1122'
        verify = input("Adding records to "+cusName+" are you sure?(y/n)")
        if verify == 'y' or verify == 'Y':
            mainProg(cusName,authKey)
        else:
            print("Program Terminated")
    
    if comp == 2:
        cusName = 'sprinklr'
        authKey = 'LUrqgCXgzE'
        verify = input("Adding records to "+cusName+" are you sure?(y/n)")
        if verify == 'y' or verify == 'Y':
            mainProg(cusName, authKey)
        else:
            print("Program Terminated")



#------
