from pydantic import BaseModel, ValidationError
from typing import List


# с помощью pydantic мы можем провалидировать вложенные структуры данных
class Tag(BaseModel):
    id: int
    tag: str


class City(BaseModel):
    city_id: int
    name: str
    tags: List[Tag]


incoming_json = """
{
    "city_id": "123",
    "name": "Moscow",
    "tags": [
        {"id": 1, "tag": "capital"}, 
        {"id": 2, "tag": "big city"}
    ]
}
"""
try:
    city = City.parse_raw(incoming_json)
except ValidationError as e:
    print("Exception", e.json())
else:
    print(city)  # city_id=123 name='Moscow' tags=[Tag(id=1, tag='capital'), Tag(id=2, tag='big city')]
    print(city.tags[1].tag)  # big city
    tag = city.tags[1]
    # можем какие-то части преобразовать в json
    print(tag.json())  # {"id": 2, "tag": "big city"}
