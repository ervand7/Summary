try:
    1 / 1

# можем кортежем прописать несколько исключений
except (KeyError, IndexError):
    print('LookupError')

# исполняется в случае, если код правильный и не понадобилось обрабатывать исключение
else:
    print('else worked')

# исполняется в конце в любом случае, не зависимо ни от чего
finally:
    print('finally worked')

# else worked
# finally worked
