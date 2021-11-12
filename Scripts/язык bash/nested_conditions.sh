#! /bin/bash
echo "Введите марку телефона"
read brand
# || - логиское или
if [ $brand == "samsung" ] || [ $brand == "nokia" ] || [ $brand == "huawei" ] || [ $brand == "iphone" ]; then
  case $brand in
    samsung)
      echo "Скидка на телефоны $brand - 30%";;
    nokia)
      echo "Скидка на телефоны $brand - 10%";;
    huawei)
      echo "Скидка на телефоны $brand - 200%";;
    *)
    echo "На этот вид товаров скидок нет";;
  esac
else
  echo "$brand - это не марка телефона"
fi



echo "Введите марку телефона"
read brand
if [ $brand == "samsung" ] || [ $brand == "nokia" ] || [ $brand == "huawei" ] || [ $brand == "iphone" ]; then
