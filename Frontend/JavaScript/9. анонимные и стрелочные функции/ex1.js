"use strict";


// создаем анонимную функцию и на месте ее вызывем
(function () {
    console.log("это анонимная функция");
})();


// присваиваем переменной значение анонимной функции
let anonym = function () {
    console.log("это анонимная функция");
}

anonym()


// Вызов функции при помощи setTimeout
setTimeout(
    function () {
        console.log("это анонимная функция");
        },
    1000
);


// пример стрелочной функции
let turnout = () => console.log('это стрелочная функция');
turnout();


// возвращаемое значение в стрелочной функции
let some_turnout = () => 'это стрелочная функция';
console.log(some_turnout());

// передача аргументов в стрелочную функцию
let my_turnout= (a, b) => a + b;
console.log( my_turnout(2, 3))  // 5