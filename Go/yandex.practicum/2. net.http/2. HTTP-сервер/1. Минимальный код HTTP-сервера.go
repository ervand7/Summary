package main

import (
	"net/http"
)

// HelloWorld — обработчик запроса.
func HelloWorld(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("<h1>Hello, World</h1>"))
}

func main() {
	/*
		Маршрутизация запросов обработчику.
		Вызов функции http.HandleFunc() означает, что запросы
		к корню URL ("/") будет обрабатывать функция HelloWorld.
	*/
	http.HandleFunc("/", HelloWorld)

	/*
		Затем вызывается функция http.ListenAndServe(), которая принимает
		запросы к порту 8080. Это блокирующий вызов. Функция принимает
		запросы в цикле. Вместе с выходом из функции завершится программа.
		Функция может вернуть только ошибку error,
		вызванную, например, системным сбоем.

		Запуск сервера с адресом localhost, порт 8080:
	*/
	http.ListenAndServe(":8080", nil)
}
