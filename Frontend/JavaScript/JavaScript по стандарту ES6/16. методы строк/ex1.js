"use strict";


/*
Все строки в JS представлены в кодировке UTF-16, даже
если в браузере html имеет другую кодировку.

Также стоит помнить о том, что строки в JS - это неизменяемый тип данных.
То есть мы не сможем по индексу изменить строку.
 */



// ========== экранирование ==========
let myString = 'Hello! \nI \' am Ivan. Вот новый символ \tтабуляции, обратный слеш \\ и символ \u00A9 копирайта'
console.log(myString)



// ========== length ==========
console.log(myString.length)  // 86



// ========== обращение по индексам ==========
console.log(myString[21])         // В
console.log(myString.charAt(21))  // В



// ========== перебол элементов через for of ==========
for (let ch of 'Hello')
    console.log(ch)
/*
H
e
l
l
o
 */



// ========== toLowerCase, toUpperCase ==========
console.log('Hello'.toLowerCase())  // hello
console.log('Hello'.toUpperCase())  // HELLO



// ========== indexOf, lastIndexOf ==========
let a = '<span class="clock">12:34</span>'
console.log(a.indexOf('clock'))    // 13
console.log(a.indexOf('span', 2))  // 27
console.log(a.indexOf('div'))      // -1

// пример использования indexOf при обходе через цикл
let indx = -1
while (true) {
    indx = a.indexOf('span', indx + 1)
    if (indx == -1) break
    console.log(indx)
}
/*
1
27
 */

// lastIndexOf работает так же как и indexOf, только начинает искать с конца строки
console.log(a.lastIndexOf('span'))  // 27



// ========== includes, startsWith, endsWith ==========
let b = '<span class="clock">12:34</span>'
console.log(b.includes('span'))      // true
console.log(b.includes('<span>'))    // false
console.log(b.includes('clock', 20)) // false

console.log(b.startsWith('span'))    // false
console.log(b.startsWith('<span'))   // true
console.log(b.endsWith('span>'))     // true



// ========== slice, substring, substr ==========
console.log(b.slice(0, 5))    // <span
console.log(b.slice(6, 11))   // class
console.log(b.slice(12))      // "@clock">12:34</span>
console.log(b.slice(-7, -1))  // </span

// substring работает так же как и slice, тольку тут можно прописывать start > end
console.log(b.substring(6, 11))   // class
console.log(b.substring(11, 6))   // class

console.log(b.substr(6, 13)) // class="clock" (старт и кол-во символов после него)
console.log(b.substr(12))          // "clock">12:34</span> (старт и до конца)



// ========== коды символов (codePointAt) ==========
for (let ch of 'Америка')
    console.log(ch.codePointAt(0))
/*
1040
1084
1077
1088
1080
1082
1072
 */



// ========== localeCompare ==========
console.log('Америка'.localeCompare('Japan'))  // -1



// ========== trim ==========
console.log('     hello       '.trim())  // hello (убирает пробелы до и после)



// ========== repeat ==========
console.log('Abc'.repeat(5))  // AbcAbcAbcAbcAbc