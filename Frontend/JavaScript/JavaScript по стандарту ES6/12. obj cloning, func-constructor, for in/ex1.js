"use strict";


/*
 Это клонирование - не deep. Вложенные словари не будут скопированны.
 Будет скопированна только ссылка наних
 */
let book = {
    title: 'название',
    author: 'автор',
    nPages: 0,
    price: 0,
    size: {height: 100, wight: 50}

};

let lib = {};
for (let key in book) {
    lib[key] = book[key];
    console.log(key + ': ' + lib[key]);
}


// делаем глубокое (рекурсивное) копирование
function cloneDeepObj(dest, obj) {
    for (let key in obj) {
        if ((typeof obj[key]) == 'object') {
            dest[key] = cloneDeepObj({}, obj[key]);
        } else {
            dest[key] = obj[key];
        }
    } return dest;
}

let some = cloneDeepObj({}, book);
book.size.height = 0  // проверяем, что несмотря на это, в some будет другое значение (100)
console.log(some)  // [Log] {title: "название", author: "автор", nPages: 0, price: 0, size: {height: 100, wight: 50}} (ex1.js, line 37)


// создание объекта через функцию-конструктор
function Constructor(title, author, price) {
    if (new.target == undefined)  // если вызвали без new
        return new Constructor(title, author, price)  // добавим new автоматически
    // this = {}; (неявно)
    this.title = title;
    this.author = author;
    this.price = price;
    // return this; (неявно)
}
let newBook = new Constructor("Му-му", 'Тургенев', 10)
let newBook2 = new Constructor("Онегин", 'Пушкин', 20)
console.log(newBook)  // Constructor {title: "Му-му", author: "Тургенев", price: 10}
console.log(newBook2)  // Constructor {title: "Онегин", author: "Пушкин", price: 20}
// вызов без new
let newBook3 = Constructor('Онегин', 'Пушкин');
console.log(newBook3)  // Constructor {title: "Онегин", author: "Пушкин", price: undefined}

// использование анонимных функций в качестве конструкторов
let someCar = new function () {
    this.model = 'reno';
    this.go = function () {
        console.log('машина едет');
    }
}
someCar.go();  // машина едет
console.log(someCar);  // {model: "reno", go: function}
