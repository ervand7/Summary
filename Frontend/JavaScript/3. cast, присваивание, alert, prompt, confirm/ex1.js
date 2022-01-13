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