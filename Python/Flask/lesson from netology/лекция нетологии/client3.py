import requests

HOST = 'http://127.0.0.1:5051'

resp_check_validate = requests.post(
    f'{HOST}/test_post/12',
    headers={'user-agent': 'Ervand'},
    json={
        'text': 'some text',
        'priority': 22,
        'expire_date': '2021-12-12',
        'visible_for': 'all'
    }
)

json = resp_check_validate.json()

a = 0
