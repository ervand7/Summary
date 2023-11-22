def find_diffs(src, dst, path=""):
    diffs = []

    if type(src) != type(dst):
        diffs.append(f"{path}: Type mismatch ({type(src)} != {type(dst)})")
        return diffs

    if isinstance(src, dict):
        if len(src) != len(dst):
            diffs.append(f"{path}: Different number of keys ({len(src)} != {len(dst)})")

        for key in src:
            if key not in dst:
                diffs.append(f"{path}.{key}: Key missing in dst")
            else:
                diffs.extend(find_diffs(src[key], dst[key], f"{path}.{key}"))

    elif isinstance(src, list):
        if len(src) != len(dst):
            diffs.append(f"{path}: Different list lengths ({len(src)} != {len(dst)})")

        for i in range(len(src)):
            diffs.extend(find_diffs(src[i], dst[i], f"{path}[{i}]"))

    else:
        if src != dst:
            diffs.append(f"{path}: Value mismatch ({src} != {dst})")

    return diffs


json_obj1 = {"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", ["cooking", {1: 1}]]}
json_obj2 = {"name": "John", "age": 30, "city": "New York", "hobbies": ["reading", ["cooking", {1: 3, 2: 2}]]}

print(find_diffs(json_obj1, json_obj2))
# ['.hobbies[1][1]: Different number of keys (1 != 2)', '.hobbies[1][1].1: Value mismatch (1 != 3)']