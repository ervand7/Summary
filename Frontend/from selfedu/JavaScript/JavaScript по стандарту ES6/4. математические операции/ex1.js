"use strict";

/*
в бинарном операторе <-> все строки приводятся к числам.
То есть, если бы x = "2.8", то он был бы приведен к типу Number
 */
let x = 2.8, y = 7.3;
console.log(x - y);  // -4.5

// унарный оператор <->
let q = true, w = null, e = undefined;
console.log(-q);  // -1
console.log(-w);  // -0
console.log(-e);  // NaN
console.log(typeof -q, typeof -w, typeof -e, );  // number number number

// часто вместо такого преобразования к Number
let val = "56";
let dig = Number(val)
// делают такое:
let dig2 = +val

// здесь сначала произойдет 3 + 2, а затем 5 + "2" = "52"
console.log(3 + 2 + "2");  // 52

// строка преобразуется к Number и во время деления
console.log("2" / 5);  // 0.4

// остаток от деления
console.log(8 % 3)  // 2

// возведение в степень
console.log(2 ** 2)  // 4

// ++ (инкремент) и -- (декремент)
let counter = 2, cnt = 5;
counter++;  // или можно записать как ++counter
cnt--;  // или можно записать как --cnt
console.log(counter, cnt)  // 3 4

// но есть различия между ++n и n++. В ++n инкремент исполняется раньше
let a, b, c = 10, d = 10;
a = c++;
b = ++d;
console.log(a, b, c, d)  // 10 11 11 11

// ================== СРАВНЕНИЕ ==================
console.log(2 > 1);  // true
console.log(2 == 1);  // false
console.log(2 != 1);  // true

let result = 7 > 5;  // result = true
console.log(result);  // true

console.log('Я' > 'А');  // true
console.log('Кот' > 'Код');  // true
console.log('Сонный' > 'Сон');  // true

// особенности
console.log(true == 1);  // true
console.log(false == 0);  // true
console.log(null == undefined);  // true
console.log(null >= undefined);  // false
console.log(null <= undefined);  // false
console.log(null > 0);  // false
console.log(null == 0);  // false
console.log(null >= 0);  // true

/*
строгое сравнение с учетом типов данных производится
через === и !==
*/
console.log(true === 1);  // false
console.log(false === 0);  // false
console.log("5" === 5);  // false
console.log(null === undefined);  // false
console.log("5" !== 5);  // true
console.log(null !== undefined);  // true