# Вариант 1. Конкатенация (плюсуем строки)
name = "Eric"
print("Hello " + name + ", would you like to learn some Python today?")

# Вариант 2. f-строка
print(f"Hello {name}, would you like to learn some Python today?")

# Вариант 3. Функция format
print("Hello {}, would you like to learn some Python today?".format(name))

# Вариант 4. Форматирование через %
print("Hello %s, would you like to learn some Python today?" % name)

# результат всех 4 вариантов будет одинаковым:
# “Hello Eric, would you like to learn some Python today?”
