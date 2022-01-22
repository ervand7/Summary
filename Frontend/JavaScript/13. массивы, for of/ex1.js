"use strict";


// ========== ОДНОМЕРНЫЕ МАССИВЫ ==========
let ar = [1, 2, 3, 4]
console.log(ar[0])  // 1
console.log(ar[550])  // undefined

ar[2] = 'груша'
console.log(ar)  // [1, 2, "груша", 4]

ar[999] = 'мы'  // что невозможно в python

console.log(ar.length)  // 1000

for (let i = 0; i < ar.length; ++i)
    console.log(ar[i])
/*
1
2
груша
4
<995 undefined>
мы
 */


// обрезаем массив
ar.length = 2
console.log(ar)  // [1, 2]


// искусственно увеличиваем длину массива
ar.length = 6
for (let i = 0; i < ar.length; ++i)
    console.log(ar[i])
/*
1
2
<4 undefined>
 */


/*
 for of
Следует запомнить: for in - для объектов, for of - для массивов
 */
for (let value of ar)
    console.log(value)
/*
1
2
<4 undefined>
 */


// метод push
ar = [1, 2, 3, 4, 5]
ar.push('Привет')
console.log(ar)  // [1, 2, 3, 4, 5, "Привет"]


// метод pop
let delElem = ar.pop()
console.log(delElem)  // Привет
console.log(ar)  // [1, 2, 3, 4, 5]


/*
 методы shift/unshift используются, чтобы удалить/вставить
 чье-то на место нулевого элемента
 */
let shifted = ar.shift()
console.log(shifted)  // 1
console.log(ar)  // [2, 3, 4, 5]

ar.unshift('яблоко')
console.log(ar)  // ["яблоко", 2, 3, 4, 5]


// ========== МНОГОМЕРНЫЕ МАССИВЫ ==========
let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
console.log(matrix[2][0])  // 7
// перебор элементов многомерного массива через for of
for (let i of matrix) {
    let columns = ''
    for (let j of i)
        columns += j
    console.log(columns)
}
/*
123
456
789
 */

// перебор элементов многомерного массива обычным циклом
for (let i = 0; i < matrix.length; ++i) {
    let columns = ''
    for (let j = 0; j < matrix[i].length; ++j)
        columns += matrix[i][j]
    console.log(columns)
}
/*
123
456
789
 */