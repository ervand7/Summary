from pydantic import BaseModel, ValidationError, Field

"""
pydantic решает проблему snake case/camel case. Он автоматически переводит
camel case в snake case
"""


class City(BaseModel):
    city_id: int
    name: str = Field(alias="cityFullName")


incoming_json = """
{
    "city_id": "132",
    "cityFullName": "Moscow"
}
"""
try:
    city = City.parse_raw(incoming_json)
except ValidationError as e:
    print("Exception", e.json())
else:
    print(city)  # city_id=132 name='Moscow'
    print(city.json(by_alias=True))  # {"city_id": 132, "cityFullName": "Moscow"}
    print(city.json(by_alias=True, exclude={"city_id"}))  # {"cityFullName": "Moscow"}
