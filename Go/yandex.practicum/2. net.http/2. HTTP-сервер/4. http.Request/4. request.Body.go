package main

import (
	"fmt"
	"io"
	"net/http"
)

func BodyHandler(w http.ResponseWriter, r *http.Request) {
	// читаем Body
	b, err := io.ReadAll(r.Body)
	fmt.Println(b, err)
	// обрабатываем ошибку
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	// продолжаем обработку
	// ...
}
