a = {i: pow(i, 2) for i in range(1, 11)}
print(a)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

#  the above written expression is in analog of:
b = {}
for i in range(1, 11):
    b[i] = pow(i, 2)

print(b)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

c = {word: len(word) for word in ['hello', 'world', 'hi']}
print(c)  # {'hello': 5, 'world': 5, 'hi': 2}

data = {
    'Джозеф Безос': '177',
    'ИлоН МаСк': '126',
    'Бернар АрнО': '150',
    'Билл ГейтС': '124'
}

new_data = {key.title(): int(value) for key, value in data.items()}
print(data)  # {'Джозеф Безос': '177', 'ИлоН МаСк': '126', 'Бернар АрнО': '150', 'Билл ГейтС': '124'}
print(new_data)  # {'Джозеф Безос': 177, 'Илон Маск': 126, 'Бернар Арно': 150, 'Билл Гейтс': 124}
