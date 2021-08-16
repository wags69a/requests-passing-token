# requests-passing-token
#Use Case Description
Using import requests, capture the access token and pass it to the next "GET" API 
The first part of the script captures the access token. My customer token was only good for 180 seconds. 

The second part of the script uses the token to allow access for the get request.

token[17:3563] you need to look at your token as see how big it is. This works for mine, your legnth may be different. This only captures the body of the token in between the double quotes. It seems that the python script will add its own double quotes to the request. Watch out for the plus sign, at first, it disappeared in the request but a space sign fixed it. For troubleshooting use print(header) to see what you are sending. 

In my exmple, the base url, check number, client id and secert are blanked out, you will need to get this information from your customer. 

This is version 1 of this script, in version 2, I hope to read a list of check numbers so that I can get the output to more than one at a time.

#UPDATE
Version 2 is working. It passes the timed token and printouts multiple APIs.

#Installation
I used postman in the customer environment. You will have to adjust to your customer.

#Usage
This code is meant to be used in a customer environment. It will change from each user. The URL should match what the customer gives you to test. The access token is the 1st API to use. The userID and password need to come from the customer. The URLs will come from the customer also.

#DevNet Sandbox
Does not apply at this time as this example is a real customer.

#Known issues
The tokens are all differnt, you must figure it out to use this script.

#Getting help
Contact the owner if he is not too busy.

#Credits and references
The Cisco requests library
The book, automate the boring stuff with python.
The customer's developer portal.

#Best Practice
Creat the .text file local to the python script.

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/wags69a/requests-passing-token)
