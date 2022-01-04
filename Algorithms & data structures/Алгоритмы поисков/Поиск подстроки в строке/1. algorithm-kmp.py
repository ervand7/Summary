# Алгоритм Кнута-Морриса-Пратта (КМП-алгоритм): поиск подстроки в строке
# Сложность алгоритма O(m), где m - длина entry


entry = "лилила"
text = "лилилось лилилась"

len_entry = len(entry)
len_text = len(text)


def get_pi():
    pi = [0] * len_entry
    j, i = 0, 1
    while i < len_entry:
        entry_j = entry[j]
        entry_i = entry[i]
        if entry_j == entry_i:
            pi[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                pi[i] = 0
                i += 1
            else:
                j = pi[j - 1]

    return pi


text_pointer = 0
entry_pointer = 0
while text_pointer < len_text:
    if text[text_pointer] == entry[entry_pointer]:
        text_pointer += 1
        entry_pointer += 1
        if entry_pointer == len_entry:
            print("образ найден")
            break
    else:
        if entry_pointer > 0:
            pi = get_pi()
            entry_pointer = pi[entry_pointer - 1]
        else:
            text_pointer += 1

if text_pointer == len_text and entry_pointer != len_entry:
    print("образ не найден")
