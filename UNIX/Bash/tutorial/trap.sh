#!/bin/bash
# Well article here:
# https://rtfm.co.ua/bash-ispolzovanie-komandy-trap-dlya-perexvata-signalov-preryvaniya-processa/
count=0

trap 'echo "Hello"; exit 1' 2

while [ $count -lt 100 ]; do
  sleep 1
  ((count++))
  echo $count
done
