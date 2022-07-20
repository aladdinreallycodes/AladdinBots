import time
import requests
import re

def main():
    transform()
    add()

def transform():
    f = open("requests.txt", "r")
    links = f.readlines()
    f = open("transformed.txt", "w")

    for url in links:
        link = requests.get(url)
        linkhtml = link.text

        if "/featured" in url:
            url = url.replace("/featured", "")

        if "/channel/" in url:
            print(url.strip())
            f.write(url.strip()+"\n")

        else:
            channelID = re.search(r'(?<="channelUrl":").*?(?=",)', linkhtml)
            print(channelID[0])

            f.write(channelID[0]+"\n")

    print("Finished Transforming")

def add():
    # Crimson = 1726
    # Sprinklr = 1712

    # cusName = 'crimson'
    # authKey = 'Rhbvcjy1122'

    # cusName = 'sprinklr'
    # authKey = 'LUrqgCXgzE'

    f = open("transformed.txt", "r")
    links = f.readlines()

    cusName = 'crimson'
    authKey = 'LUrqgCXgzE'

    API_ENDPOINT = "http://"+cusName+":"+authKey+"@localhost:8080/"+cusName+"/youtube/main/channels"

    print("Modifying " + cusName)

    for x in range(len(links)):
        time.sleep(1)
        links[x] = links[x].strip()
        stringToExport = (
            '\n{\n\t\"addAll\": {\n\n\t\t"url": "'+links[x]+'"\n\t}\n}')
            #deleteAll to delete
        data = stringToExport
        #print(data)
        r = requests.post(url=API_ENDPOINT, data=data)
        print(links[x] + " " + r.text)

if __name__ == "__main__":
    main()