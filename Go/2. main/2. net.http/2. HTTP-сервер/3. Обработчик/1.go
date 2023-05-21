package main

import (
	"log"
	"net/http"
)

// MyHandler Обработчик может выглядеть, например, так:
type MyHandler struct {
	Templ []byte
}

// Главное, чтобы он реализовал интерфейс Handler выполнив метод ServeHTTP:
func (h MyHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Write(h.Templ)
}

func main() {
	// Тогда обработчик можно использовать как поле структуры http.Server:
	handler1 := MyHandler{
		Templ: []byte("Hola, Mundo"),
	}
	server := &http.Server{
		Handler: handler1,
	}
	// вызов ListenAndServe — блокирующий, последний в программе
	// возникающие ошибки на серверных машинах пишут в системный лог,
	// а не в стандартную консоль ошибок,
	// поэтому обычно вызывают вот так
	log.Fatal(server.ListenAndServe())

}
