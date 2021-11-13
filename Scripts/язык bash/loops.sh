#! /bin/bash

for n in 1 2 3; do
    echo $n
done

echo "Пробел"

for (( i = 0; i < 10; i++ )); do
    echo $i
done

echo "Пробел"

n=1
while [ $n -lt 4 ]; do
  echo $n
  n=$(( $n+1 ))

done