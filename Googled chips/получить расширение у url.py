# Получить расширение у url
from urllib.parse import urlparse
from os.path import splitext, basename

picture_page = "http://distilleryimage2.instagram.com/da4ca3509a7b11e19e4a12313813ffc0_7.jpg"
disassembled = urlparse(picture_page)
# print(disassembled)

# Теперь у нас отдельно есть и filename (имя ссылки), и file_ext (расширение)
# print(splitext(basename(disassembled.path)))
filename, file_ext = splitext(basename(disassembled.path))
print(filename)
print(file_ext)

