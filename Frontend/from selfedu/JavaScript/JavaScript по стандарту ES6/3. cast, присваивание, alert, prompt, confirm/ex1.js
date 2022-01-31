"use strict";

// приведение к типу String
let a = true;
a = String(a);
console.log(a);  // true
console.log(typeof a);  // string

// приведение к типу Number
let b = "123";
let c = Number(b);
console.log(c);  // 123
console.log(typeof c);  // number

//JS автоматически приводит строки к number при таких ситуациях
console.log("6" / "3");  // 2

// конкатенация возможна в следующих формах
console.log("6" + "3");  // 63
console.log(6 + "3");  // 63
console.log("6" + 3);  // 63

// другие примеры преобразований различных типов данных к Number
console.log(Number("   123   "));  // 123 (начальные и конечные пробелы убираются)
console.log(Number("123z"));       // NaN (ошибка чтения числа)
console.log(Number(true));         // 1
console.log(Number(false));        // 0

// преобразования к Boolean
console.log(Boolean(1))  // true
console.log(Boolean(0))  // false
console.log(Boolean("0"))  // true
console.log(Boolean("Привет"))  // true
console.log(Boolean(""))  // false

// другие варианты работы с оператором присваивания
let f, g, h;
f = g = h = 2 + 2;
console.log(f, g, h)  // 4  4  4

let t, u = 1;
let o = 3 - (t = u + 1);
console.log(t, u, o);  // 2 1 1

// alert. Модальное окно с заданным текстом
alert("Hello");

// prompt. Модальное окно с вводом информации и дефолтным значением
let age = prompt("Сколько вам лет?", "18");
console.log(age);

// confirm
let isCar = confirm("У тебя есть машина?");
console.log(isCar);