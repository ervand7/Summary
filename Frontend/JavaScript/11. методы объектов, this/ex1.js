"use strict";


// любое свойство, которое является ссылкой на функцию, называется методом объекта
let car = {
    model: 'toyota',
    color: 'black',
    go: function () {
        console.log('машина едет')
    },
    superGo: function (driverName) {
        console.log(`Водитель ${driverName} едет на машине`)
    },
    // упрощенный вариант написания
    superPuperGo(driverName) {
        console.log(`Водитель ${driverName} едет на машине`)
    },
    // с помощью инструкции this мы можем в методе обратиться к другому свойству объекта
    getModel() {
        return this.model
    }

};
// вызов метода
car.go();  // машина едет

// добавление метода
car.stop = function () {
    console.log('машина остановлена')
}
car.stop();  // машина остановлена

car.superGo('Vasya')  // Водитель Vasya едет на машине
car.superPuperGo('Vasya')  // Водитель Vasya едет на машине

console.log(car.getModel());  // toyota