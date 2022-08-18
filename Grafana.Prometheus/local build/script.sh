#! /bin/bash

# while выполняет код пока условие верно. А until наоборот

n=1
while [ $n -lt 400 ]; do
  echo "Hello 3.14" | curl --data-binary @- http://localhost:9091/metrics/job/prometeus
  echo "number is $n"
  n=$(($n + 1))
  sleep 1

done
