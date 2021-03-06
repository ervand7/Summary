#! /bin/bash

# Условные операторы
file=/Users/dasaagadzanan/Desktop/Summary/UNIX/vim.txt
username=далее
if grep -i $username $file; then
  echo "Пользователь найден в системе!"
  cat $file
else
  echo "Пользователь не найден в системе!"
fi

# Сравнение чисел
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

# Сравнение строк через \> и \<
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

# Операторы &&, ||, -o
echo "Введите ваш возраст"
read age
if [ $age -le 1 ] || [ $age -lt 2 ]; then
  echo "Вы еще грудничок"
elif [ $age -ge 5 ] && [ $age -lt 12 ]; then
  echo "Вы еще ребенок"
elif [ $age -ge 12 ] && [ $age -lt 18 ]; then
  echo "Вы подросток"
elif [ $age -ge 18 ] && [ $age -lt 60 ]; then
  echo "Вы уже взрослый"
elif [ $age -ge 100 -o $age -gt 101 ]; then
  echo "Вы долгожитель"
else
  echo "Вы пенсионер"

fi
