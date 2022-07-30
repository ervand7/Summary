package main

import (
	"fmt"
	"net/http"
)

/*
SimpleFunc Не всегда нужен Handler со сложной структурой и внутренним состоянием.
Достаточно, чтобы для него был реализован метод ServeHTTP.
Для таких случаев в пакете http декларирован тип:
type HandlerFunc func(ResponseWriter, *Request)

И для этого типа интерфейс Handler уже реализован выполнением метода ServeHTTP.
Поэтому можем взять любую функцию подходящей сигнатуры
*/
func SimpleFunc(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Something"))
}
func main() {

	// и сделать из неё http.Handler простым приведением типов:
	handler2 := http.HandlerFunc(SimpleFunc)
	fmt.Println(handler2)
}
