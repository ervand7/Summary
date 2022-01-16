"use strict";

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
while ((summa += item++) < 100);
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