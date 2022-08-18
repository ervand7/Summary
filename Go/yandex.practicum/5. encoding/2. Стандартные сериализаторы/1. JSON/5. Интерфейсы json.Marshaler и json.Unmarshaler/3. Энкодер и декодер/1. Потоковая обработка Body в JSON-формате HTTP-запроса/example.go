package main

import (
	"encoding/json"
	"net/http"
)

type SomeType struct{}

func Handler(w http.ResponseWriter, r *http.Request) {
	var v SomeType // целевой объект

	if err := json.NewDecoder(r.Body).Decode(&v); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}
	// дальнейшая обработка запроса
}
