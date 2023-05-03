# хорошая статья: https://librerussia.github.io/python-3-rabota-s-zip-arkhivami-modul-zipfile.html
import os
import zipfile

archive = os.path.join(os.getcwd(), 'archive.zip')
file_in_zip = 'example.py'

print(zipfile.is_zipfile(archive))
my_archive = zipfile.ZipFile(archive, 'r')
print(my_archive)
print('______________________________________')

my_archive.printdir()
print('______________________________________')

# вытягиваем файлы в обычную папку из изначального zip-архива
storage = os.path.join(os.getcwd(), 'сюда вытягиваем файлы из zip')
example_py = my_archive.extract(file_in_zip, storage)
my_archive.extractall(storage)

# вытягиваем файл 'example.py' из изначального архива 'archive.zip', создаем новый
# архив 'new.zip' и записываем в него 'example.py'
with zipfile.ZipFile('new.zip', mode='w') as new_zip:
    new_zip.write(example_py)

# Для записи всех файлов в директории можно воспользоваться функцией os.walk:
# Создание нового архива
third_zip = zipfile.ZipFile('third.zip', mode='w')
# Список всех файлов и папок в директории 'Новая папка'
for root, dirs, files in os.walk('Новая папка'):
    for file in files:
        third_zip.write(os.path.join(root, file))
third_zip.close()
