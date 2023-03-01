import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Query parameters
address = "Missouri University of Science and Technology"
params = {} # dict()

params['address'] = address
params['key'] = 42

url = 'http://py4e-data.dr-chuck.net/json?' + urllib.parse.urlencode(params)

print(url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

try:
    js = json.loads(data)
except:
    js = None

print(js['results'][0])
