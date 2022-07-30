package main

import (
	"encoding/json"
	"net/http"
)

type Subj struct {
	Product string `json:"name"`
	Price   int    `json:"price"`
}

/*
JSONHandler В этом примере сначала устанавливаем заголовки, потом кодируем
данные структуры Subj в формат JSON и пишем их в ResponseWriter.
*/
func JSONHandler(w http.ResponseWriter, req *http.Request) {
	// сначала устанавливаем заголовок Content-Type
	// для передачи клиенту информации, кодированной в JSON
	w.Header().Set("content-type", "application/json")
	// устанавливаем статус-код 200
	w.WriteHeader(http.StatusOK)
	// собираем данные
	subj := Subj{"Milk", 50}
	// кодируем JSON
	resp, err := json.Marshal(subj)
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}
	// пишем body ответа
	w.Write(resp)
}
