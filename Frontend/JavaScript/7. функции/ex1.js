"use strict";

// в JS можно вызывать функцию до ее определения
outLog();  // Вызов функции

// определение функции
function outLog() {
    console.log("Вызов функции")
}

outLog();  // Вызов функции


// ========== ПЕРЕДАЧА ПАРАМЕТРОВ ==========
function myLog(msg) {
    console.log(msg)
}

myLog("Привет");  // Привет


function showMessage(from, text) {
    let msg = from + ', ' + text.toLocaleLowerCase();
    console.log(msg)
}

showMessage('Вася', 'Привет')  // Вася, привет


// ========== return ==========
function abs(x) {
    if (x < 0) x = -x;
    return x;
}

let res = abs(-5);
console.log(res);  // 5

// функция с применением тернарного оператора
function abs2(x) {
    return (x < 0) ? -x : x;
}

let res2 = abs2(-5);
console.log(res2);  // 5