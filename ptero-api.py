# This code uses requests for pterodactyl panel.

import hmac
import hashlib
import base64
import requests

url = ''
private = ''
public = ''

message = bytes(url, "utf-8")
secret = bytes(private, "utf-8")

signature = str(base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest()))
sig = public+"."+signature[2:][:-1]

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'Authorization':"Bearer {}".format(sig)}
r = requests.get(url, headers=headers)
print(signature)
print(sig)

