#! /bin/bash

# while выполняет код пока условие верно. А until наоборот

n=1
while [ $n -lt 4 ]; do
  echo "number is $n"
  n=$(($n + 1))

done

n=1
until [ $n -ge 10 ]; do
  echo $n
  n=$(($n + 1))

done
