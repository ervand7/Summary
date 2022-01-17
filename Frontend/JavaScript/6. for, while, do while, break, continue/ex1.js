"use strict";
/*
Примеры из этого файла продемонстрированны на языке Python
в модуле ec1.py
 */

// while. Пример 1
let s = 0, i = 1;
while (i <= 1000 && s < 6) {
    s += 1 / i;
    ++i;
}
console.log(s);  // 6.004366708345567


/* while. Пример 2 (не рекомендуется). Все в одну строчку, без тела цикла.
Вся сумма вычисляется при задаче условия
 */
let summa = 0, item = 1;
while ((summa += item++) < 100) ;
console.log(summa);  // 105


// for. Пример 1
let mySum = 0;
for (let myItem = 1; myItem <= 1000; ++myItem)
    mySum += 1 / myItem;
console.log(mySum)  // 7.485470860550343


// for. Пример 2
/*
Внимание, инициализацию счетчика x мы можем записать и так:
let f, k = 0.5, b = 2;
let x = 0;
for (;x <= 1; x += 0.1) {
    f = k * x + b;
    console.log(f)
}
также можем увеличение счетчика поместить в тело цикла:
let f, k = 0.5, b = 2;
let x = 0;
for (;x <= 1;) {
    f = k * x + b;
    console.log(f)
    x += 0.1
}
возможен и такой вариант:
let f, k = 0.5, b = 2;
let x = 0;
for (;;) {
    if (x <= 1) break;
    f = k * x + b;
    console.log(f)
    x += 0.1
}
 */
let f, k = 0.5, b = 2;
for (let x = 0; x <= 1; x += 0.1) {
    f = k * x + b;
    console.log(f)
}
/*
2
2.05
2.1
2.15
2.2
2.25
2.3
2.35
2.4
2.45
2.5
 */


/*
do while. Отличается от циклов for и while тем, что сначала выполняет
тело цикла, а только потом проверяет условие цикла
 */
const PSW = "password";
let psw = null;
// сначала выполняем тело цикла. Пользователь вводит пароль
do {
    psw = prompt("Введите пароль", "");
}
// и если пароль неверный, запускаем цикл сначала
while (psw != PSW);
console.log("Вы вошли в систему!")


// вложенные циклы:

let counter = 0, some = 10, some2 = 5;
for (let i = 1; i <= some2; ++i)
    for (let j = 1; j <= some; ++j)
        counter += i * j
console.log("counter = " + counter)  // 825


// оператор break
// 1) чтобы прервать внутренний цикл:
let _counter = 0, _some = 10, _some2 = 5;
for (let i=1; i <= _some2; ++i)
    for (let j = 1; j <= _some; ++j) {
        if (j == 5) break
        _counter += i * j
    }
console.log("counter = " + _counter)  // 150
// 2) чтобы прервать внешний цикл:
let _counter_ = 0, _some_ = 10, _some2_ = 5;
myVariable: for (let i=1; i <= _some2_; ++i)
    for (let j = 1; j <= _some_; ++j) {
        if (j == 5) break myVariable;
        _counter_ += i * j
    }
console.log("counter = " + _counter_)  // 10


// оператор continue
for (let i = -5; i <= 5; ++i) {
    if (i == 0) continue;
    console.log("i = " + i)
}
/*
i = -5
i = -4
i = -3
i = -2
i = -1
i = 1
i = 2
i = 3
i = 4
i = 5
 */