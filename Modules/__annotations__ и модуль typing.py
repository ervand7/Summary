# 2 статьи про модуль typing:
# https://habr.com/ru/company/lamoda/blog/432656/
# https://habr.com/ru/company/lamoda/blog/435988/

def render_int(num: int) -> str:
    return str(num)


print(render_int.__annotations__)  # {'num': <class 'int'>, 'return': <class 'str'>}
