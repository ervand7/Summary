#! /bin/bash

# объявление функции
list_files() {
  echo "Выводим содержимое каталога"
  cd ~/.ipython/
  ls
}

# вызов функции
list_files