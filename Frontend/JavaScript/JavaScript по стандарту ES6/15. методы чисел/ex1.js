"use strict";


/*
 Number - числовой тип.
 Пример того, как в JS можно задавать числа
 */
let a1 = 1e9         // 1 000 000 000 (экспоненциальная запись)
let a2 = 0.e3        // 0.5 * 1000 = 500
let a3 = 1e-6        // 0.000001
let a4 = 0xff        // шестнадцатиричная запись (аа = 255)
let a5 = 0b11111111  // двоичная запись десятичного числа 255
let a6 = 0o377       // восьмеричная форма записи числа 255

/*
 какие особенности нужно знать при работе с числами:
 1) есть предел больших чисел, которые мы можем записать
так как существует 64-битный форматхранения, где 52 бита отводятся
для хранения цифр, 11 - для хранения положения десятичной точки (для
целых чисел там 0), 1 знаковый бит.
То есть мы не сможем создать число 1e500, оно будет Infinity.

 2) дробные числа представляются в приближенном виде.
let rez = 0.1 + 0.2
console.log(rez)  // 0.30000000000000004
Соответственно, мы не сможем сделать такое сравнение:
console.log(rez == 0.3)  // false
 */



// ========== toString ==========
let num = 255
// параметром должна быть система счисления
console.log(num.toString(16), typeof num.toString(16))  // ff "string"
console.log(num.toString(2))  // 11111111
// если не передаем параметр, то получаем просто строку в десятеричной системе
console.log(num.toString(), typeof(num.toString()))  // 255 "string"

// можем также вызывать этот метод от числа
console.log(127..toString(16))  // 7f



// ========== floor, ceil, round, toFixed ==========
console.log(Math.floor(1.5))  // 1
console.log(Math.ceil(1.5))  // 2
console.log(Math.round(1.4))  // 1
console.log(Math.round(1.5))  // 2
console.log(1.23556.toFixed(2))  // 1.24



// ========== isFinite, isNaN ==========
console.log(isNaN(NaN))          // true
console.log(isNaN('1'))   // можно привести к числу, поэтому false
console.log(isNaN(2))     // это число, поэтому false
console.log(isNaN('abc')) // true

console.log(isFinite('15'))  // true
console.log(isFinite('str')) // false, потому что это не число
console.log(isFinite(Infinity))     // false

// применить isFinite на практике можно таким образом:
let n = prompt('Enter a number', '')
if (n.length > 0 && isFinite(n)) console.log('это число')
else console.log('это не число')



// ========== parseInt, parseFloat ==========
console.log(parseInt('12pt'))  // 12
console.log(parseInt('100%'))  // 100
console.log(parseInt('340px')) // 340

console.log(parseFloat('12.5pt'))  // 12.5
console.log(parseFloat('90.5%'))   // 90.5
console.log(parseFloat('+30.5px')) // 30.5



// ========== random ==========
for (let i = 0; i < 10; ++i)
    console.log(Math.random())
/*
0.15944426133400347
0.19806403543310247
0.6960976637046057
0.9473023838973958
0.3136809494937197
0.37985184959371565
0.48422925170416575
0.5385673724510313
0.6803729040198365
0.5420607403675879
 */



// ========== max, min ==========
console.log(Math.max(1, 2, 0, -10, 5, 7))  // 7
console.log(Math.min(1, 2, -10, 5))  // -10



// ========== pow ==========
console.log(Math.pow(2, 10))  // 1024
console.log(Math.pow(8, 1/3))  // 2
