"use strict";

let x = -5;
if (x < 0) x = -x;  // меняем знак на противоположный
console.log("|x| = " + x)


let y = -5
if (y < 0) console.log("отрицательное");
else console.log("не отрицательное");


/*
если после условия мы хотим прописать несколько действий
то прописываем их в {}. Так как прописывать несолько условий
можно только в {}
*/
let n = 0, sgn = 0;
if (n < 0) {
    sgn = -123;
    console.log("n был отрицательным", sgn)
}
else
    if (n > 0) {
        sgn = 321;
        console.log("n был положительным", sgn)
    }
    // тут мы могли бы и не ставить фигкрные скобки
    else {console.log("n равен 0", sgn)}

// тернарный оператор
let age = 20;
let accessAllowed = (age > 18) ? true: false
console.log(accessAllowed)  // true

// ОПЕРАТОРЫ !, && и ||
// оператор ! меняет условие на противоположное (имеет высочайший приоритет)
if(!0) console.log("Привет")  // Привет
if(" ") console.log("Не пустая строка дает true")  // Строка '0' дает true
if(!"") console.log("123123123")  // 123123123


// оператор && (имеет след приоритет после !)
let a = 4;
if (a >= 2 && a<=7) console.log("a попадает в [2; 7]");
else console.log("a не попадает в [2; 7]")


// оператор || (наименьший приоритет)
let w = -4;
if (w < 2 || a>7) console.log("w не попадает в [2; 7]");
else console.log("w попадает в [2; 7]")


/*
оператор switch используется тогда, когда нужно из множества
возможных вариантов выбрать какой-то один.
Мы должны после каждого case прописывать break, иначе сработают
все операторы6 которые будут идти после оператора с верным условием.
 */
let item = 3;
switch (item) {
    case 1: console.log("item = 1"); break;
    case 2: console.log("item = 2"); break;
    case 3: console.log("item = 3"); break;
    case 4: console.log("item = 4"); break;
    // default - это необязательное условие
    default: console.log("item имеет другое значение");
}