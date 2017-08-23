# Python Standard Modules
import sys
import json

# PyPi Modules (must be installed with pip command)
import requests

# Arguments
username = str(sys.argv[1])
text = str(sys.argv[2])
count = int(sys.argv[3])

# API Endpoints
url = "https://%s.sarahah.com" % username
sendMessage = "https://%s.sarahah.com/Messages/SendMessage" % username
thankyou = "http://www.sarahah.com/messages/thankyou"

file = open("proxies.json", "r")
proxies = json.load(file.read())
file.close()

s = requests.Session()

def spam(page):
    recipId = page.text.split('<input id="RecipientId" type="hidden" value="')[1].split('"')[0]
    csrftoken = page.text.split('<input name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
    
    payload = {
        "__RequestVerificationToken": csrftoken,
        "userId": recipId,
        "text": text
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "%s.sarahah.com" % username,
        "Origin": url,
        "Referer": url,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.8',
        'X-Requested-With': 'XMLHttpRequest'
    }

    for c in range(1, count+1):
        res = s.post(sendMessage, data=payload, headers=headers, proxies=proxies)
        if res.status_code == 200:
            print('Successfully spammed "%s" to %s %s time(s)' % (text, username, str(c)))   
        else:
            print("Spam failed.")
            break

if len(sys.argv) != 4:
    print('Invalid usage.\n Correct arguments:\n username, message, count \n\nExample usage:\n python VoteBot.py crocbuzz "Hello dear friend" 10')
else:
    if (text == "") or (count <= 1):
        print('Error:\nthe text arugment must be surrounded in quotation marks\nthe count argument must be greater than 1')
    else:
        r = s.get(url, proxies=proxies)
        if r.status_code == 200:
            print("Running Sarahah spam bot...")
            spam(r)
        else:
            print('Connection error, perhaps the server is down?')
