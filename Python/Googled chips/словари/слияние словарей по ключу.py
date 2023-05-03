# Слияние словарей по ключу
dictionary1 = {123: ('qwe', 'asd', 888)}
dictionary2 = {123: ('zxc', 'xcv')}


def merge_dict(dict1, dict2):
    """Merge dictionaries and keep values of common keys in list"""
    result_dict = {**dict1, **dict2}
    for key, value in result_dict.items():
        if key in dict1 and key in dict2:
            result_dict[key] = [value, dict1[key]]
    return result_dict


print(merge_dict(dictionary1, dictionary2))


# Упрощенный варант
def merge_dict2(dict1, dict2):
    """Merge dictionaries and keep values of common keys in list"""
    for key, value in dict2.items():
        if key in dict1 and key in dict2:
            dict2[key] = [value, dict1[key]]
    return dict2


print(merge_dict2(dictionary1, dictionary2))


# Попробуем объединить 3 словаря по ключу
dct1 = {3213: ('qw34e', 'asd', 888)}
dct2 = {3213: ('hkh', 'xcv')}
dct3 = {3213: (('as', 'sdf'), 'gngn')}


def merge_dict3(dict1, dict2, dict3):
    """Merge dictionaries and keep values of common keys in list"""
    final_dict = {**dict1, **dict2, **dict3}
    for key, value in final_dict.items():
        if key in dict1 and key in dict2 and key in dict3:
            final_dict[key] = [value, dict1[key], dict2[key]]
    return final_dict


print(merge_dict3(dct1, dct2, dct3))
