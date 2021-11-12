#! /bin/bash
echo "Введите марку телефона"
read brand

case $brand in
samsung)
  echo "Скидка на телефоны $brand - 30%";;
nokia)
  echo "Скидка на телефоны $brand - 10%";;
huawei)
  echo "Скидка на телефоны $brand - 200%";;
# else
*)
  echo "На этот вид товаров скидок нет";;
esac