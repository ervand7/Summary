#! /bin/bash

# условные операторы
file=/Users/dasaagadzanan/Desktop/Summary/UNIX/vim.txt
username=далее
if grep -i $username $file; then
  echo "Пользователь найден в системе!"
  cat $file
else
  echo "Пользователь не найден в системе!"
fi

# сравнение чисед
num1=10
num2=20
if [ $num1 -eq $num2 ]; then
  echo "Значения равны"
elif [ $num1 -gt $num2 ]; then
  echo "Значение 1 больше значения 2"
elif [ $num1 -lt $num2 ]; then
  echo "Значение 1 меньше значения 2"
else
  echo "Неопознанное значение"
fi

# сравнение строк
str1="Программирование на Ba"
str2="Программирование на Bas"

if [ "$str1" \> "$str2" ]; then
  echo "Первая строка больше"
elif [ "$str1" \< "$str2" ]; then
  echo "Первая строка меньше"
elif [ "$str1" == "$str2" ]; then
  echo "Строки равны"
else
  echo "Неопознанное значение"
fi

# запуск через:
# $ chmod +x if_script.sh
# $ ./if_script.sh