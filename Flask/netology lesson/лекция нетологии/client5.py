import requests

HOST = 'http://127.0.0.1:5051'

resp = requests.get(
    f'{HOST}/check-password2?login=test_user&password=такой_то_пароль',
)
json = resp.json()

a = 0
