# обсуждение: https://stackoverflow.com/questions/23049767/parsing-http-response-in-python
from urllib.request import urlopen
import json

# Get the dataset
url = 'https://httpbin.org/get'
response = urlopen(url)

# Convert bytes to string type and string type to dict
string = response.read().decode('utf-8')
json_obj = json.loads(string)
print(json_obj)
# {'args': {}, 'headers': {'Accept-Encoding': 'identity', 'Host': 'httpbin.org',
# 'User-Agent': 'Python-urllib/3.8', 'X-Amzn-Trace-Id': 'Root=1-607dd322-25b115ef1a23fa3f16773daf'},
# 'origin': '93.157.169.19', 'url': 'https://httpbin.org/get'}

print(json_obj['headers']['User-Agent'])  # Python-urllib/3.8
