from typing import Any


def diff_obj(first: Any, second: Any):
    if first == second:
        return None
    if isinstance(first, float) and isinstance(second, float) and math.isclose(first, second):
        return None
    if first is None:
        return f'added {second}'
    if second is None:
        return f'removed {first}'

    if isinstance(first, dict) and isinstance(second, dict):
        keys = set(first.keys()).union(second.keys())
        result = dict()
        for key in keys:
            diff = diff_obj(first.get(key), second.get(key))
            if diff:
                result[key] = diff
        return result if result else None

    if isinstance(first, list) and isinstance(second, list):
        result = list()
        first, second = set(first), set(second)
        for value in first.union(second):
            diff = diff_obj(
                value if value in first else None,
                value if value in second else None
            )
            if diff:
                result.append(diff)
        return result if result else None

    return f'changed {first} => {second}'
