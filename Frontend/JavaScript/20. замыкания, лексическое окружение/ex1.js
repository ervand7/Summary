"use strict";


function createCounter() {
    let count = 0
    return function () {
        return count++
    }
}

let a = createCounter()
console.log(a())  // 0
console.log(a())  // 1
console.log(a())  // 2

let b = createCounter()
console.log(b())  // 0
console.log(b())  // 1
console.log(b())  // 2