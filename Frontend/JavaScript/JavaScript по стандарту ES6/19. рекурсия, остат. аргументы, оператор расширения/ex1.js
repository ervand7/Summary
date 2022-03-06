"use strict";


// ========== РЕКУРСИЯ ==========
// пример 1
function pow(x, n) {
    if (n <= 0) return 1
    else return x * pow(x, n-1)
}
console.log(pow(2, 3))  // 8


// пример 2
let company = {
    sales: [{name: 'Иван', salary: 1000}, {name: 'Михаил', salary: 600}],
    development: {
        sites: [{name: 'Евгений', salary: 2000}, {name: 'Алексей', salary: 1800}],
        internals: [{name: 'Федор', salary: 1300}]
    }
}

function sumSalary(department) {
    if (Array.isArray(department)) {
        return department.reduce((prev, current) => prev + current.salary, 0)
    }
    else {
        let sum = 0
        for (let prop in department) {
            sum += sumSalary(department[prop])
        }
        return sum
    }
}

console.log(sumSalary(company))              // 6700
console.log(sumSalary(company.sales))        // 1600
console.log(sumSalary(company.development))  // 5100



/*
Важно понимать, что оператор <...> может использоваться
и для остаточных аргументов и для расширения
 */
// ========== ОСТАТОЧНЫЕ АРГУМЕНТЫ ==========
function sumAll(...args) {
    let sum = 0
    for (let val of args)
        sum += val
    return sum
}
console.log(sumAll(1, 2))       //3
console.log(sumAll(1, 2, 3, 4)) // 10



// ========== ОПЕРАТОР РАСШИРЕНИЯ ==========
let items = [1, 2, 3, 4, 5]
let digs = [-1, 0, 6, 10, 101]
let max = Math.max(...items, ...digs)
console.log(max)  // 101