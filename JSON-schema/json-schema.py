# pip install jsonschema
# Все элементы схемы описаны здесь: https://habr.com/ru/post/495766/
# Шикарный сайт с лучшим объяснением, он же и официальная документация:
# https://json-schema.org/understanding-json-schema/index.htmlz

# Примр использования валидации
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
            },
        "age": {"type": "number",
                "minimum": 18,
                "maximum": 110
                },
        "role": {
            "type": "string",
            "enum": ["admin", "user"]
            }
        }
    }

message = {"name": "Vasya", "age": 15, "role": "user"}

validate(message, schema)
