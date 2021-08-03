# requests-passing-token
Using import requests, capture the access token and pass it to the next "GET" API 

The first part of the script captures the access token. My customer token was only good for 120 seconds. 

The second part of the script uses the token to allow access for the get request.

token[17:3563] you need to look at your token as see how big it is. This works for mine, your legnth may be different. This only captures the body of the token in between the double quotes. It seems that the python script will add its own double quotes to the request. Watch out for the plus sign, at first, it disappeared in the request but a space sign fixed it. For troubleshooting use print(header) to see what you are sending. 

In my exmple, the base url, check number, client id and secert are blanked out, you will need to get this information from your customer. 

This is version 1 of this script, in version 2, I hope to read a list of check numbers so that I can get the output to more than one at a time.
