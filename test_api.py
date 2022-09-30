from flask import jsonify
import requests
import json 	
import requests

url = "https://youtube138.p.rapidapi.com/video/details/"

querystring = {"id":"ld4nzao5XAc"}

headers = {
	"X-RapidAPI-Key": "2f205d967cmshffde6f247a6d5cap12aec9jsn1ac72dd8e0db",
	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response_str = response.text


response_json = response.json()
print(response_json["stats"])
with open('api.json', 'w') as file:
    json.dump(response_json, file, indent=4)