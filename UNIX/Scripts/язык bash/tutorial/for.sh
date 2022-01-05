#! /bin/bash

# Варианты написания цикла for
for item in Первый Второй Третий; do
  echo "$item элемент"
done

for n in 1 2 3; do
  echo $n
done

for i in {89..98}; do
  echo $i
done

# что-то не работает
for s in {0..20..2}; do
  echo $s
done

: '
Итерируемся по файлу.
Для начала переопределяем сепаратор, который по умолчанию разделяет
текст не по строкам, а по одному слову.'

IFS=$'\n'
file="file.txt"
for row in $(cat $file); do
  echo "$row"
done

# обход файлов папки
dir=/Users/dasaagadzanan/*
for file in $dir; do
  if [ -d $file ]; then
    echo "$file - директория"
  elif [ -f $file ]; then
    echo "$file - файл"
  else
    echo "Неизвестная сущность"
  fi
done

# второй вариант написания цикла, в стиле зыка C
for ((i = 1; i <= 10; i++)); do
  echo "Значение i = $i "
done
