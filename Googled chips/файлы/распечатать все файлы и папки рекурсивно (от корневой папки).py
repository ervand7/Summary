# Распечатать все файлы и папки (от корневой папки)
import os


def show_all_directory():
    for dir_path, dir_names, file_names in os.walk(".."):  # . - текущий каталог; .. - родительский каталог
        # перебрать каталоги
        for dir_name in dir_names:
            print("Каталог:", os.path.join(dir_path, dir_name))
        # перебрать файлы
        for filename in file_names:
            print("Файл:", os.path.join(dir_path, filename))


show_all_directory()
