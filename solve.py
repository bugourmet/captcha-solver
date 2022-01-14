import requests
import base64
import json
import urllib.request
import io


def solvecaptcha(imgurl):
    with urllib.request.urlopen(imgurl) as url:
        f = io.BytesIO(url.read())
        encoded_string = base64.b64encode(f.read())
    
    url = 'https://api.apitruecaptcha.org/one/gettext'
    data = { 'userid':'YOUR_USER_ID', 'apikey':'YOUR_API_KEY',  'data':str(encoded_string)[2:-1],  'case':'mixed'}
    r = requests.post(url = url, json = data)
    jsonresponse = json.loads(r.text)
    return(jsonresponse['result'])

solvecaptcha("https://image.url/file.png")