package main

import (
	"fmt"
	"net/http"
)

func HeaderHandler(w http.ResponseWriter, r *http.Request) {
	// заголовки доступны методом Header.Get
	ct := r.Header.Get("Content-Type")
	fmt.Println(ct)
	// для типового запроса ct примет значение "text/html; charset=UTF-8"
	// продолжаем обработку
	// ...
}
