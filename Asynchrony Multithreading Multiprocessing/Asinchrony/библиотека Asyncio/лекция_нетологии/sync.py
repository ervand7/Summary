import requests
import time

start = time.time()
for person_id in range(1, 11):
    url = f'http://swapi.dev/api/people/{person_id}'
    person_data = requests.get(url).json()
    print(person_id, person_data)

print(time.time() - start)
