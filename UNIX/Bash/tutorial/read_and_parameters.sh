#! /bin/bash

# за $0 всегда зарезервированно имя файла
echo "Название файла: $0"

# параметр -n позволяет начать ввод с той же строки
echo -n "Как вас зовут? "
# с помощью read записываем пользовательский ввод в переменную Name
read Name
echo "Привет, $Name"

# параметры. Так мы можем передавать параметры
echo "$(($1 $2 $3))"
# после чего запуск скрипта будет <./read_and_parameters.sh 12 + 4>

: '
Так мы можем вводить неограниченное кол-во аргументов и далее их выводить
Но в данном случае эта конструкция нам просто выведет всегдааргументы,
которые мы ввели при запуске скрипта'
args=("$@")
echo $@
# "echo $#" выводит кол-во введенных аргументов
echo $#
