import requests

# resp = requests.get('http://127.0.0.1:5051/health').json()
# print(resp)


# resp = requests.get('http://127.0.0.1:5051/users/1').json()
# print(resp)


resp = requests.post(
    'http://127.0.0.1:5051/users/',
    json={
        'username': 'test',
        'password': 'sgdsppo34FET32325',
        'email': 'test@test.test'
    }).json()
print(resp)
