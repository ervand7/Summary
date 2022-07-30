package main

import (
	"fmt"
	"net/http"
)

/*
Метод mux.HandleFunc позволяет зарегистрировать в качестве обработчика
любую функцию с сигнатурой func(ResponseWriter, *Request):
*/

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
		fmt.Fprintf(w, "Welcome to the home page!")
	})
}
