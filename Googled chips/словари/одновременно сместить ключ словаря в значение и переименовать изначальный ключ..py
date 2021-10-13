# Одновременно сместить ключ словаря в значение и переименовать изначальный ключ.
# А так же избежать ошибки "dictionary changed size during iteration"
# https://coderoad.ru/11941817/%D0%9A%D0%B0%D0%BA-%D0%B8%D0%B7%D0%B1%D0%B5%D0%B6%D0%B0%D1%82%D1%8C-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B8-RuntimeError-dictionary-changed-size-during-iteration

lst = [{'qwe': 123}, {'asd': 345}, {'zxc': 567}]
for dct in lst:
    for str_key in list(dct):  # Оборачивая i в list мы избег. ош.: dictionary changed size during iteration
        dct['file_name'] = str_key
# print(lst)
for big_dct in lst:
    for list_of_keys in list(big_dct):  # Оборачивая i в list мы избег. ош.: dictionary changed size during iteration
        if 'file_name' not in list_of_keys:
            big_dct.pop(list_of_keys)
print(lst)


