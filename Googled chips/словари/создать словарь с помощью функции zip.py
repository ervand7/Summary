# С помощью функции zip создать словарь
names = ['Tom', 'Dick', 'Harry']
ages = [50, 35, 60]

new_dict = dict(zip(names, ages))
print(new_dict)