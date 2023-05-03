# обсуждение: https://stackoverflow.com/questions/23049767/parsing-http-response-in-python
from urllib.request import urlopen
import json

# Get the dataset
url = 'https://httpbin.org/get'
response = urlopen(url)

# Convert bytes to string type and string type to dict
string = response.read().decode('utf-8')
"""
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.8", 
    "X-Amzn-Trace-Id": "Root=1-62224a9c-304e4a44767ca96c5e72a7da"
  }, 
  "origin": "93.157.169.19", 
  "url": "https://httpbin.org/get"
}
"""

json_obj = json.loads(string)
"""
{
'args': {}, 'headers': 
    {'Accept-Encoding': 'identity', 
    'Host': 'httpbin.org', 'User-Agent': 'Python-urllib/3.8', 
    'X-Amzn-Trace-Id': 'Root=1-62224a9c-304e4a44767ca96c5e72a7da'}, 
'origin': '93.157.169.19', 'url': 'https://httpbin.org/get'
}
"""

print(json_obj['headers']['User-Agent'])  # Python-urllib/3.8
