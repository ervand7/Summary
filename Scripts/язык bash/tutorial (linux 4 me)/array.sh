#! /bin/bash

Array=(2 34 565 8)
Array2=(34 3 five)
# вывод всех элементов массива
echo ${Array[@]}
echo ${Array2[@]}

# вывод индексов массива
echo ${!Array[@]}
echo ${!Array2[@]}

# вывод элементов по индексу
echo ${Array[2]}
echo ${Array2[0]}

# вывод длины массива
echo ${#Array[@]}
echo ${#Array2[@]}

# вывод кол-ва символов определенного элемента
echo ${#Array[1]}
echo ${#Array2[2]}

# устанавливаем новые значения у конкретных индексов
Array[3]=four
Array2[2]=5
echo ${Array[@]}
echo ${Array2[@]}

# перебор элементов массива в цикле for
for i in ${!Array[@]}; do
    echo "${Array[$i]}"
done