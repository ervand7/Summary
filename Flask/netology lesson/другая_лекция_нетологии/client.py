import requests

HOST = 'http://127.0.0.1:8000'

# resp = requests.get(f'{HOST}/users/4')
# print(resp.status_code)
# print(resp.json())

post_resp = requests.post(f'{HOST}/users/', json={
    'username': 'pupkqwein_1qwe9944',
    'password': '12qwe34',
    'email': 'pupkqwedsfgfadin2@mail.ru'
})
print(post_resp.json())


