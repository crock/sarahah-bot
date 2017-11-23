#! /usr/bin/env python3
# Python Standard Modules
import sys
import os
import json
import random
import threading
from queue import Queue
import time

# PyPi Modules (must be installed with pip command)
import requests

# User Modules
from lib.proxy import *

# Arguments
username = str(sys.argv[1])
text = str(sys.argv[2])
count = int(sys.argv[3])

# API Endpoints
url = "https://%s.sarahah.com" % username
sendMessage = "https://%s.sarahah.com/Messages/SendMessage" % username
thankyou = "http://www.sarahah.com/messages/thankyou"

s = requests.Session()
q = Queue()
print_lock = threading.Lock()

def get_tokens(page):
    recipId = page.text.split('<input id="RecipientId" type="hidden" value="')[1].split('"')[0]
    csrftoken = page.text.split('<input name="__RequestVerificationToken" type="hidden" value="')[1].split('"')[0]
    
    return (recipId, csrftoken)

def get_payload(tokens):
    return {
        "__RequestVerificationToken": tokens[1],
        "userId": tokens[0],
        "text": text,
        "captchaResponse": None

    }

def get_headers():
    return {
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

def requestJob(proxy):
    if check_proxy(proxy):
        with print_lock:
            print("%s is working" % proxy)

def threader():
    while True:
        item = q.get()
        requestJob(item)
        q.task_done()

def main():
    proxies = get_proxy_list()
    if proxies is not None:
        print("Checking and filtering out bad proxies...")
        start = time.time()

        for x in range(10):
            t = threading.Thread(target = threader)
            t.daemon = True
            t.start()

        for item in proxies:
            q.put(item)

        q.join()

        total = str(time.time()-start)
        numBad = len(bad_proxies)
        numProxies = len(proxies)
        print("\nSearched %s proxies and filtered out %s bad proxies in %s seconds" % (numProxies, numBad, total))

    headers = get_headers()

    for c in range(1, count+1):
        tempSess = requests.Session()
        i = random.randrange(0, good_proxies.__len__())
        sess = set_proxy(tempSess, good_proxies[i])
        res = sess.get(url, headers=headers)
        # tempFile = open('test.html', 'w')
        # tempFile.write(res.text)
        # tempFile.close()
        tokens = get_tokens(res)
        payload = get_payload(tokens)
        res = sess.post(sendMessage, data=payload, headers=headers)
        if res.status_code == 200:
            print('Successfully spammed "%s" to %s %s time(s)' % (text, username, str(c)))   
        else:
            print("Spam failed.")
            break

if __name__ == "__main__":
    main()