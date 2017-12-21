import requests
import json
while(True):
    string=input("enter the word:").split(" ")
    if(What==string[0]):
        url = "https://en.wikipedia.org/w/api.php?action=query&titles=coconut&prop=revisions&rvprop=content&format=json"
        frt="json"
        data={"titles":string[2],"key":frt}
        response = requests.get(url,data)
        json_data = json.loads(response.text)
        valu=json_data["query"]["pages"]
        valu1=list(valu.values())
        valu2=valu1[0]['revisions']
        print(valu2[0]['*'])
    elif(Where == string[0]):
        url="https://maps.googleapis.com/maps/api/geocode/json"
        frt="AIzaSyAg78naGXpoydKvRX7Z2bJIwlNOvKP7JsM"
        data={"address":string[2:],"key":frt}
        response=requests.get(url,data)
        json_data = json.loads(response.text)
        valu=json_data['results']
        print(valu[0]['formatted_address'])
    elif(How == string[0]):
        url = "http://www.omdbapi.com/"
        data={"t":string[2],"apikey": "450b2283"}
        response = requests.get(url,data)
        json_data = json.loads(response.text)
        print(json_data)
        
    
        

    

