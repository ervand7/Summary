"""Пишем синхронный код с использованием генераторов."""
import requests


def people(n):
    for person_id in range(1, n):
        url = f'http://swapi.dev/api/people/{person_id}'
        person_data = requests.get(url).json()
        yield person_data


for person in people(10):
    print(person)
