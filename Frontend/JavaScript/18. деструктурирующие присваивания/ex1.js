"use strict";


let cars = ['yaguar', 'porshe', 'mersedes']
let [car1, car2, car3] = cars
console.log(car1, car2, car3)  // yaguar, porshe, mersedes


// можем присвоить не всем переменным
let [some, some2] = cars
console.log(some, some2)  // yaguar, porshe


// деструктуризация строки
let [firstName, middleName, lastName] = 'Иван Иванович Иванов'.split(' ')
console.log(firstName, middleName, lastName)  // Иван Иванович Иванов


// разная деструктуризация массива
let [fr1, fr2m, ...last] = ['Груша', 'Слива', 'Яблоко', 'Персик', 'Виноград']
console.log(fr1, fr2m, last)  // Груша Слива ["Яблоко", "Персик", "Виноград"]
let [a, b, c, d] = ['Груша', 'Слива']
console.log(a, b, c, d)  // Груша Слива undefined undefined
