import jsonschema
from flask import request, jsonify


def validate(schema):
    """
    Валидатор входящих запросов.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                jsonschema.validate(
                    request.get_json(),
                    schema=schema,
                )
            except jsonschema.ValidationError as er:
                return jsonify({'success': False, 'description': er.message}), 400
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator
