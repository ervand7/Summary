import requests

HOST = 'http://127.0.0.1:5051'

resp = requests.post(
    f'{HOST}/test_post/42',
    headers={'test_header': 'hello', 'user-agent': 'Ervand'},
    json={'key': 'any client data'}
)
json = resp.json()

a = 0
