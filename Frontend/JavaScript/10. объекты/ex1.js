"use strict";

// создание
let some = {}
let some2 = new Object();


let book = {
    title: 'название',
    author: 'автор',
    nPages: 0,
    price: 0
}

console.log(book.title);  // название
console.log(book.price);  // 0

book.isSelled = false
console.log(book.isSelled);  // false

// удаление
delete book.nPages;
console.log('nPages' in book);  // false

book["size book"] = {height: 100, wight: 50}
console.log(book["size book"]);  // {height: 100, wight: 50}


// пример с prompt
let keyName = prompt('Что вы хотите узнать о книге?', 'title');
console.log(book[keyName]);


// вариант создания объекта через функцию
let car = createCar('toyota', 'black');
function createCar(model, color) {
    return {
        model,
        color
    };
}
console.log(car);  // {model: "toyota", color: "black"}


// вывод всех значений объекта через цикл
for (let key in book) {
    console.log(book[key])
}
