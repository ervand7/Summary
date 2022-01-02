# Алгоритм Бойера-Мура-Хорспула. Худший вариант - O(n*m), лучший - O(n/m)

entry = "kasha"
len_entry = len(entry)  # число символов в образе


# Этап 1: формирование таблицы смещений
def get_dict_offsets():
    unique_entry_symbols = set()  # уникальные символы в образе
    dict_offsets = {}  # словарь смещений

    for i in range(len_entry - 2, -1, -1):  # итерации с предпоследнего символа
        if entry[i] not in unique_entry_symbols:  # если символ еще не добавлен в таблицу
            dict_offsets[entry[i]] = len_entry - i - 1
            unique_entry_symbols.add(entry[i])
    if entry[len_entry - 1] not in unique_entry_symbols:  # отдельно формируем последний символ
        dict_offsets[entry[len_entry - 1]] = len_entry

    dict_offsets['*'] = len_entry  # смещения для прочих символов

    return dict_offsets


print(get_dict_offsets())

# Этап 2: поиск образа в строке
text = "dasha dasha kasha"
len_text = len(text)

if len_text >= len_entry:
    i = len_entry - 1  # счетчик проверяемого символа в строке

    while i < len_text:
        pointer_1 = 0
        pointer_2 = 0
        flBreak = False
        for pointer_2 in range(len_entry - 1, -1, -1):
            if text[i - pointer_1] != entry[pointer_2]:
                if pointer_2 == len_entry - 1:
                    offset = get_dict_offsets()[text[i]] \
                        if get_dict_offsets().get(text[i], False) \
                        else get_dict_offsets()['*']  # смещение, если не равен последний символ образа
                else:
                    offset = get_dict_offsets()[entry[pointer_2]]  # смещение, если не равен не последний символ образа

                i += offset  # смещение счетчика строки
                flBreak = True  # если несовпадение символа, то flBreak = True
                break

            pointer_1 += 1  # смещение для сравниваемого символа в строке

        if not flBreak:  # если дошли до начала образа, значит, все его символы совпали
            print(f"образ найден по индексу {i - pointer_1 + 1}")
            break
    else:
        print("образ не найден")
else:
    print("образ не найден")
