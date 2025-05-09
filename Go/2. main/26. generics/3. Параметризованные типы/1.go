package main

// Декларацию типа тоже можно параметризировать. Вот пример параметризованного типа:

// Vector — имя для слайса элементов любого типа, важно, чтобы они были одинаковы.
type Vector[T any] []T

// Как и в случае с вызовом функции, параметризованный тип для декларации
// переменной нужно инстанцировать:
// v — переменная типа Vector из int
var vInt Vector[int]

// VectorInt другой вариант определения — с дополнительным типом VectorInt
type VectorInt Vector[int]

var vInt2 VectorInt
