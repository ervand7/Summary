def diff_two_obj(src: Any, dst: Any):
    if src == dst:
        return None
    if isinstance(src, float) and isinstance(dst, float) and math.isclose(src, dst):
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
