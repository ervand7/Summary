#! /bin/bash

# цикл for
for item in Первый Второй Третий
do
  echo "$item элемент"
done

# итерируемся по файлу
# для начала переопределяем сепаратор, который по умолчанию разделяет
# текст не по строкам, а по одному слову
IFS=$'\n'
file="file.txt"
for row in $(cat $file)
do
  echo "$row"
done

# обход файлов папки
dir=/Users/dasaagadzanan/*
for file in $dir
do
  if [ -d $file ]; then
    echo  "$file - директория"
  elif [ -f $file ]; then
    echo  "$file - файл"
  else
    echo  "Неизвестная сущность"
  fi
done

# второй вариант написания цикла, в стиле зыка C
for (( i = 1; i <= 10; i++ )); do
    echo "Значение i = $i "
done

# запуск через:
# $ chmod +x for_script.sh
# $ ./for_script.sh