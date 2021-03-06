import requests
import time
import csv
import json

url = "https://{BASE URL}/oauth/accesstoken"

payload = 'grant_type=client_credentials&client_id={ID}&client_secret={PASSWORD}'
headers = {
    'x-api-key': '{API NUMBER}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
token = response.text
time.sleep(1)

# API number
myfile = open("checks.txt", "r")
for line in myfile:
    url2 = "https://{BASE URL}/checking/"+format(line).strip()
    payload2 = {}
    headers2 = {
        'Authorization': "Bearer+" + token[17:3608],
        'x-api-key': 'API NUMBER'
    }
    print(line)
    time.sleep(1)
    print(url2)
#myfile.close()
    time.sleep(2)
    response2 = requests.request("GET", url2, headers=headers2, data=payload2)
    print(response2.text)
    time.sleep(2)


time.sleep(1)
myfile.close()
jsonout = json.dumps(response2.text)