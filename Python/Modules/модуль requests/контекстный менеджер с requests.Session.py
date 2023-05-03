# хорошая официальная документация (источник этого конспекта): https://requests.readthedocs.io/en/master/user/advanced/
# import requests module
import requests

# Let’s persist some cookies across requests:
s = requests.Session()
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')
print(r.text)

s = requests.Session()
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})
# both 'x-test' and 'x-test2' are sent
response = s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
print(response)

r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
print(r.text)  # '{"cookies": {"from-my": "browser"}}'
r = s.get('https://httpbin.org/cookies')
print(r.text)  # '{"cookies": {}}'

with requests.Session() as s:
    print(s.get('https://httpbin.org/cookies/set/sessioncookie/123456789'))  # <Response [200]>
