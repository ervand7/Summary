from urllib.parse import unquote

row = '%D0%9D%D0%B0%D1%83%D1%87%D0%BD%D0%B0%D1%8F+%D1%84%D0%B0%D0%BD%D1%82%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%B0'
row_ = 'https://qwerty.asdfg.zxcvb.poiu/dfgh/1234?ghjk=vcxz&genre=%D0%9D%D0%B0%D1%83%D1%87%D0%BD%D0%B0%D1%8F+%D1%84%D0%B0%D0%BD%D1%82%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%B0&fgcefg=2016&23413412341=web'

print(unquote(row))  # Научная+фантастика
print(unquote(row_.rsplit('&', maxsplit=3)[-3][6:]))  # Научная+фантастика
