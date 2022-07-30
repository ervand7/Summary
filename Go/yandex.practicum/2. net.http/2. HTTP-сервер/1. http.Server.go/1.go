package main

import "net/http"

func HelloWorld(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("<h1>Hello, World</h1>"))
}
func main() {
	// маршрутизация запросов обработчику
	http.HandleFunc("/", HelloWorld)
	// конструируем свой сервер
	server := &http.Server{
		Addr: "mydomain.com:80",
	}
	server.ListenAndServe()
}
