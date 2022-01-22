"use strict";


// ========== splice ==========
let ar = ['Я', 'смотрю', 'этот', 'обучающий', 'урок']
/*
 1 аргумент - индекс аргумента, с которого мы будем удалять (включительно)
 2й - сколько элементов мы будем удалять начиная с этого индекса
 3й - элементы, которые будут вставлены на место удаленных
 */
ar.splice(2, 2)
console.log(ar)  // ["Я", "смотрю", "урок"]

let delElem = ar.splice(2, 1, 'это', 'классный')
console.log(delElem)  // ["урок"]
console.log(ar)  // ["Я", "смотрю", "это", "классный"]

// также мы можем с помощью splice вставлять элементы ничего не удаляя
ar.splice(1, 0, 'интересный')
console.log(ar)  // ["Я", "интересный", "смотрю", "это", "классный"]

/*
 можно встравить несколько элементов через обратныю индексацию
 Здесь мы отсчитываем 3 элемента с конца, и на их место вставляем 3 новых
 */
ar.splice(-3, 3, 'последние', 'три', 'элемента')
console.log(ar)  // ["Я", "интересный", "последние", "три", "элемента"]



// ========== slice ==========
let my_array = ['Я', 'смотрю', 'этот', 'обучающий', 'урок']
// возьмется элемен с индексом 2 и 3
console.log(my_array.slice(2, 4))  // ["этот", "обучающий"]
// возьмутся все элементы после 3 (включительно)
console.log(my_array.slice(3))  // ["обучающий", "урок"]
// возьмутся все элементы после -3 (включительно)
console.log(my_array.slice(-3))  // ["этот", "обучающий", "урок"]

// с помощью slice можно скопировать массив
let copyArr = my_array.slice()
console.log(copyArr)  // ["Я", "смотрю", "этот", "обучающий", "урок"]



// ========== concat ==========
let my_ar = [1, 2]
let new_ar = my_ar.concat([3, 4])
console.log(new_ar)  // [1, 2, 3, 4]



// ========== forEach ==========
my_array.forEach(function (i) {
    console.log(i)
})
// можно также реализовать через стрелочную функцию
my_array.forEach((i) =>
    console.log(i)
)
/*
Я
смотрю
этот
обучающий
урок
 */

// допустим, мы хотим вывести только четные значения списка
let digs = [1, 2, 3, 4, 5, 6, 7]
digs.forEach((i, index) => {
    if (i % 2 == 0) console.log(`${i} с индексом ${index}`)
})
/*
2 с индексом 1
4 с индексом 3
6 с индексом 5
 */



// ========== indexOf, lastIndexOf, includes ==========
let a = ['Я', 'смотрю', 'этот', 'обучающий', 'урок', 0, false, null]
// найдем индекс элемента 'смотрю', начиная с 0 индекса
let res1 = a.indexOf('смотрю', 0)
console.log(res1)  // 1
// найдем индекс элемента null, начиная с 0 индекса м после этого идем в самое начало массива
let res2 = a.lastIndexOf(null, 0)
console.log(res2)  // -1 (не найдено)
// проверим, есть элемент 0, начиная с 3 индекса
let res3 = a.includes(0, 3)
console.log(res3)  // true



// ========== find, findIndex ==========
// эти методы ищут только первый подходящий элемент
let cars = [
    {model: 'toyota', price: 1000},
    {model: 'opel', price: 800},
    {model: 'reno', price: 1200},
]
// найдем обхект, у которого поле price < 1000
let rez = cars.find(i => i.price < 1000)
console.log(rez)  // {model: 'opel', price: 800}

// метод findIndex делает все то же самое, но только возвращает не сам объект, а индекс
let indexRez = cars.findIndex(i => i.price < 1000)
console.log(indexRez)  // 1



// ========== filter ==========
// делает то же самое, что и find, но только ищет не первое, а все подходящие элементы
let filterRez = cars.filter(i => i.price <= 1000)
console.log(filterRez)  // [{model: "toyota", price: 1000}, {model: "opel", price: 800}]



// ========== map ==========
let myCars = ['toyota', 'opel', 'reno']
let result = myCars.map(function (i) {
    return i.length
})
console.log(result)  // [6, 4, 4]



// ========== sort ==========
let myDigs = [4, 25, 2]
myDigs.sort()  // результат будет некорректным, так как sort воспринимает все как строки
console.log(myDigs)  // [2, 25, 4]

// подправим это
myDigs.sort(
    function (a, b) {
        if (a > b) return 1  // можно вообще указать любое положительное число
        else if (a < b) return -1  // можно вообще указать любое отрицательное число
        else return 0
    }
)
console.log(myDigs)  // [2, 4, 25]

// можно переписать еще удобнее через стрелочную функцию
myDigs.sort( (a, b) => a-b)
console.log(myDigs)  // [2, 4, 25]



// ========== reverse ==========
let someDigs = [1, 4, 2, 7, 5, 9]
someDigs.reverse()
console.log(someDigs)  // [9, 5, 7, 2, 4, 1]



// ========== split/join ==========
let emailsTo = 'alex12@m.ru, hello@m.ru, world@m.ru, hi@m.ru'
let arEmails = emailsTo.split(', ', 3)
for (let email of arEmails)
    console.log(email)
/*
alex12@m.ru
hello@m.ru
world@m.ru
 */

let strEmails = arEmails.join(', ')
console.log(strEmails)  // 'alex12@m.ru, hello@m.ru, world@m.ru'



// ========== reduce/reduceRight ==========
let my_digs = [1, -2, 100, 3, 9, 54]
// подсчитаем сумму всех элементов
let mySum = my_digs.reduce((sum, current) => sum + current, 0)  // 0 - это начальное значение суммы
console.log(mySum)  // 165

// подсчитаем произведение всех элементов
let pr = my_digs.reduce((pr, current) => pr * current, 1)
console.log(pr)  // -291600

// reduceRight аналогичен reduce, только проходит по массиву справа налево



// ========== Array.isArray ==========
console.log(typeof {})  // object
console.log(typeof [])  // object

console.log(Array.isArray({}))  // false
console.log(Array.isArray([]))  // true