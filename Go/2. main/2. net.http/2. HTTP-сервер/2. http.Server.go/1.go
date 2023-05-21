package main

import (
	"net/http"
)

// HelloWorld Handler
func HelloWorld(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("<h1>Hello, World</h1>"))
}
func main() {
	// маршрутизация запросов обработчику
	http.HandleFunc("/", HelloWorld)
	// конструируем свой сервер
	server := &http.Server{
		Addr: "http://127.0.0.1:8080",
	}
	server.ListenAndServe()
}
