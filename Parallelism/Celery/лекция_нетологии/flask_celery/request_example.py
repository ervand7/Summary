import time

import requests

resp = requests.post('http://127.0.0.1:5000/comparison', files={
    'image_1': open('example/valeri_nikolaev.jpg', 'rb'),
    'image_2': open('example/zhan_zhar.jpeg', 'rb')
})
resp_data = resp.json()
print(resp_data)
task_id = resp_data.get('task_id')
print(task_id)
#


resp = requests.get(f'http://127.0.0.1:5000/comparison/{task_id}')
print(resp.json())
time.sleep(3)

resp = requests.get(f'http://127.0.0.1:5000/comparison/{task_id}')
print(resp.json())
