#change to .py to run
#get your variable for anything in quotes { }

import requests
import time


url = "https://{base url}/oauth/accesstoken"

payload='grant_type=client_credentials&client_id={client ID number}&client_secret={password}'
headers = {
  'x-api-key': '{API KEY}',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
token = response.text

time.sleep(1)



url2 = "https://{base URL}/checking/{check number}"

payload2 = {}
headers2 = {
  'Authorization': "Bearer+" + token[17:3563],
  'x-api-key': '{API KEY}'
}

response2 = requests.request("GET", url2, headers=headers2, data=payload2)

print(response2.text)

