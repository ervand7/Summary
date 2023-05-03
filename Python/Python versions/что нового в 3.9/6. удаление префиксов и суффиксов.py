# 3.8:
def strip_quotes(text: str):
    if text.startswith('"'):
        text = text[1:]
    if text.endswith('"'):
        text = text[:-1]
    return text


print(strip_quotes('"hello"'))  # 'hello'


# 3.9:
# появились функции removeprefix и removesuffix
print('"hello"'.removeprefix('"h'))  # ello"
print('"hello"'.removesuffix('llo"'))  # "he
