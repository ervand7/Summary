"use strict";


/*
Перебор элементов Map и Set осуществляется всегда в порядке добавления
этих элементов. Поэтому нельзя сказать6 что это неупорядоченные коллекции.
Но поменять порядок элементов или получить элемент напрямую по его номеру
не получится
 */



// ========== Map ==========
/*
У Map, в отличие от объектов, в качестве ключей могут выступать
не только строки, но и любые типы данных
 */
let m = new Map()
m.set('string', 'строка')
m.set(7, 'простое число')
m.set(true, {descr: 'boolean', value: true})

console.log(m.get('string'))  // строка
console.log(m.get(7))         // простое число
console.log(m.get(true))      // {descr: "boolean", value: true}

// мы можем поместить в качестве ключей даже объекты
let user = {
    name: 'Hello',
    type: 'World'
}
m.set(user, 'объект user')
console.log(m.get(user))  // объект user

// 2й вариант создания map:
let car = new Map([
    ['model', 'opel'],
    ['color', 0xff],
    ['price', 1000],
])
console.log(car)  // Map {"model" => "opel", "color" => 255, "price" => 1000}

// 3й  вариант создания map (на основе итерируемого объекта в формате key:value):
let book = {
    author: 'Пушкин',
    title: 'Онегин',
    pages: 100,
    price: 80,
}
let lib = new Map(Object.entries(book))
console.log(lib)  // Map {"author" => "Пушкин", "title" => "Онегин", "pages" => 100, "price" => 80}

// есть противоположный метод Object.entries = Object.fromEntries. Создает объект из Map
let myObject = Object.fromEntries(lib)
console.log(myObject)        // {author: "Пушкин", title: "Онегин", pages: 100, price: 80}
console.log(typeof myObject) // object

// перебор элементов Map через for of
for (let value of car) {
    console.log(value)
}
/*
["model", "opel"]
["color", 255]
["price", 1000]
 */

// перебираем только ключи
for (let value of car.keys()) {
    console.log(value)
}
/*
model
color
price
 */

// перебор элементов через forEach
car.forEach((value, key) => {
    console.log(`car[${key}] = ${value}`)
})
/*
car[model] = opel
car[color] = 255
car[price] = 1000
 */



// ========== Set ==========
/*
Коллекция Set формируется только из цникальных данных
 */
let guests = new Set()

let alex = {name: 'Alexey', old: 25}
let oleg = {name: 'Oleg', old: 32}
let masha = {name: 'Masha', old: 18}

for (let _ = 0; _ < 10; ++_)
    guests.add(alex)
    guests.add(oleg)
    guests.add(masha)

for (let guest of guests)
    console.log(guest.name)
/*
Alexey
Oleg
Masha
 */

// перебор элементов через forEach
guests.forEach((i) => {
    console.log(i.name + ': ' + i.old)
})
/*
Alexey: 25
Oleg: 32
Masha: 18
 */