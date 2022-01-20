"use strict";


function showMsg() {
    console.log('Hello!');
}

let showMsg2 = function () {
    console.log('Hello!');
};

showMsg()
showMsg2();


function agreeCookies(question, yes, no) {
    if (confirm(question)) yes();
    else no()
}

function agreeYes() {
    console.log('Вы приняли соглашение о cookies');
}

function agreeNo() {
    console.log('Вы отказались от использования cookies');
}

agreeCookies(
    'Наш сайт использует cookies. Нам нужно ваше согласие.',
    agreeYes, agreeNo)


// Пример функции в тернарном операторе
let age = prompt('Сколько вам лет?', '18');

let setAccess = (age < 18) ?
    function () {console.log('Доступ запрещен');} :
    function () {console.log('Доступ разрешен');};

setAccess();