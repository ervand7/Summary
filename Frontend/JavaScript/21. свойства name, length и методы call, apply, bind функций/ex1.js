"use strict";


// name
function showMessage(msg) {
    console.log(msg)
}
console.log(showMessage.name)  // showMessage



// length - кол-во параметров функции
function func1(a) {}
function func2(a, b) {}
function func3(a, b, ...more) {}

console.log(func1.length)  // 1
console.log(func2.length)  // 2
console.log(func3.length)  // 2



// создание свойств функции
function funcCount() {
    console.log('Вызов функции: ' + ++funcCount.counter)
}
funcCount.counter = 0

funcCount()  // Вызов функции: 1
funcCount()  // Вызов функции: 2



// реализация замыкания с помощью свойств функции
function createCounter() {
    function inner() {
        return inner.count++  // count - это свойство функции inner
    }
    inner.count = 0  // создание свойства count
    return inner
}

let myCounter = createCounter()
console.log(myCounter())  // 0
console.log(myCounter())  // 1
console.log(myCounter())  // 2
myCounter.count = 0
console.log(myCounter())  // 0
console.log(myCounter())  // 1
console.log(myCounter())  // 2



/*
 call нужен для вызова функции (в которой прописан this),
 которая расположенна в объекте
 */
let car = {
    model: 'mersedes',
    getModel(model) {
        if (model) console.log(model)
        else console.log(this.model)
    }
}

let func = car.getModel
/*
func()  // получим ошибку, так как хотим вне контекста вызвать
функцию, в которой прописан this
 */
func.call(car)  // mersedes
func.call(car, 'opel')  // opel



/*
 apply отличается от call лишь тем, что, если передаем аргументы,
 до делаем это черех массив
 */
let myMath = {
    nameObj: 'myMath',
    sum(...args) {
        return this.nameObj + ': ' + args.reduce((val, prevVal) => prevVal += val, 0)
    }
}

let sum = myMath.sum
console.log(sum.apply(myMath, [1, 2, 3, 4]))  // myMath: 10



// bind - позволяет связать контекст вызова функции до ее вызова
let mySum = myMath.sum.bind(myMath)
console.log(mySum(1, 2, 3, 4))  // myMath: 10



// дополнительное имя функции
let getName = function Name(name) {
    if (name) return name
    else return Name('other')
}

console.log(getName('Иван'))  // Иван
console.log(getName())              // other