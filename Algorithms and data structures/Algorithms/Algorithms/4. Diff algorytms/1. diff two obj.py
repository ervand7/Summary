from typing import Any


def diff_two_obj(src: Any, dst: Any):
    if src == dst:
        return None
    if src is None:
        return f'added {dst}'
    if dst is None:
        return f'removed {src}'

    if isinstance(src, dict) and isinstance(dst, dict):
        keys = set(src.keys()).union(dst.keys())
        result = dict()
        for key in keys:
            diff = diff_two_obj(src.get(key), dst.get(key))
            if diff:
                result[key] = diff
        return result if result else None

    if isinstance(src, list) and isinstance(dst, list):
        result = list()
        result.extend(
            f'removed {item}' for item in src if item not in dst)
        result.extend(
            f'added {item}' for item in dst if item not in src)
        return result if result else None

    return f'changed {src} => {dst}'


json_obj1 = {"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", ["cooking", {1: 1}]]}
json_obj2 = {"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", ["cooking", {1: 3, 2: 2}]]}

print(diff_two_obj(json_obj1, json_obj2))
# {'hobbies': ["removed ['cooking', {1: 1}]", "added ['cooking', {1: 3, 2: 2}]"]}
