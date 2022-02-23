import requests

HOST = 'http://127.0.0.1:5051'

get_resp = requests.get(f'{HOST}/status')
get_json = get_resp.json()

a = 0
