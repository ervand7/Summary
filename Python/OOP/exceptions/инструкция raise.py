# Урок 37 Инструкция raise Возбуждение / Вызов исключений в Python. Raising Exceptions Python
# Буквально возбуждаем ошибку из ничего
raise IsADirectoryError from None


# Можем прописывать один или несколько аргуентов
raise OverflowError('fatal error')
raise Exception(1, 2, 3)


# Используем псевдонимы
my_error = TypeError()
raise my_error


# Можно посмотреть документацию
error = KeyboardInterrupt
raise error(f'{error.__doc__}')


