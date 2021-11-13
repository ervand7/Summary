#! /bin/bash

Example() {
  echo "Сколько будет 2+2?"
  read answer
  if [ $answer == 4 ]; then
    echo "Ответ верный"
  else
    echo "Ответ не верный. Попробуйте еще раз."
    echo
    Example
  fi
}

echo "Пример рекурсивной функции:"
Example