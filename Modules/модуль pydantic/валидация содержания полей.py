from pydantic import BaseModel, ValidationError, Field, validator, root_validator


class City(BaseModel):
    city_id: int
    name: str = Field(alias='cityFullName')

    @validator('name')
    def name_should_contain_sbp(cls, v: str) -> str:
        if 'spb' not in v.lower():
            raise ValueError("Work with SPB!")
        return v

    @root_validator
    def name_should_contain_sbp2(cls, values):
        print('values', values)
        return values


incoming_json = """
{
    "city_id": "132",
    "cityFullName": "qwe"
}
"""
try:
    city = City.parse_raw(incoming_json)
except ValidationError as e:
    print("Exception", e.json())
else:
    print(city)
