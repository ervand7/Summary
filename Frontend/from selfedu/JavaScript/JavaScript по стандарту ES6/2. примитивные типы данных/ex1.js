"use strict";

let v = undefined;  // то же самое, что и let v;
console.log(v);  // undefined

//к числовому типу относятся и int, и float
let a = 2;
let b = 3.14;

// с помощью typeof смотрим тип переменной
console.log(typeof a);  // number

// infinity - математическая бесконечность. Это значение, которое больше любого числа
let c = 1/0;
console.log(c);  // Infinity
let d = Infinity;
console.log(d);  // Infinity
let e = -Infinity;
console.log(e);  // -Infinity

// NaN - не число. Результат ошибочной математической операции
let q = "Строка" / 2;
console.log(q);  // NaN

// string. В JS кавычки <"> равны кавычкам <'>
let msg1 = "строка 1";
let msg2 = 'строка 2';
// <`> - форматированная строка
let z = 5, x = 2; let msg3 = `z = ${z}, x = ${x}`;
console.log(msg3)  // z = 5, x = 2

// кавычка внутри строки
let cl = "class=\"my_class\"";
console.log(cl);  // class="my_class"
// или
let cl2 = 'class="my_class"';
console.log(cl2);  // class="my_class"

// bool
let isWin = true, isCheckedField = false;
console.log(isWin);  // true
console.log(isCheckedField);  // false
console.log(typeof isCheckedField);  // boolean
let isGreater = 4 > 1;
console.log(typeof isGreater);  // boolean

// null
let idProcess = null;
console.log(idProcess);  // null

// Symbol. Используется для создания уникальных идентификаторов
let id = Symbol()
let id2 = Symbol("id")
console.log(id === id2)  // false