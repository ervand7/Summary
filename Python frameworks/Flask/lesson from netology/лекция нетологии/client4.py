import requests

HOST = 'http://127.0.0.1:5051'

resp = requests.post(
    f'{HOST}/check-password',
    json={'login': 'ervand', 'password': 'такой_то_пароль'}
)
json = resp.json()

a = 0
