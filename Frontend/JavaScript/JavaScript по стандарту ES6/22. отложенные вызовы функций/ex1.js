"use strict";


/*
Синтаксис new Function. Используется крайне редко.
Здесь невозможно создать замыкание
 */
let sumTwo = new Function('a', 'b', 'return a+b')
console.log(sumTwo(1, 2))  // 3



// ========== setTimeout ==========
// пример 1
function createMsg(msg) {
    console.log(msg)
}
setTimeout(createMsg, 2000, 'Hello')  // ... Hello

// пример 2
function downloadingMsg() {
    let idLoading = setTimeout(function () {
        console.log('Идет загрузка данных...')
    }, 500)

    setTimeout(function () {
       clearTimeout(idLoading)
       console.log('Данные загружены')
    }, 2000)  // если тут будет 200, то выведется только 'Данные загружены', а таймаут для idLoading очистится
}

downloadingMsg()

// пример 3 (с алертом)
setTimeout("alert('Привет')", 1000)

// пример 4 (со стрелочной функцией)
setTimeout(() => alert('Как дела?'), 1000)



// ========== setInterval ==========
//в отличие от setTimeout вызывает функцию бесконечно
function createClock(seconds) {
    let sec = seconds

    return function () {
        sec++
        console.log('Прошло ' + sec + ' секунд')
    }
}

let clock = createClock(0)
let idClock = setInterval(clock, 1000)
setTimeout(function () {
    clearInterval(idClock)
}, 5000)