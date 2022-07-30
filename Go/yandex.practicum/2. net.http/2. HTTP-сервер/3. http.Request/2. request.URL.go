package main

import "net/http"

func QueryHandler(w http.ResponseWriter, r *http.Request) {
	// извлекаем фрагмент query= из URL запроса search?query=something
	q := r.URL.Query().Get("query")
	if q == "" {
		http.Error(w, "The query parameter is missing", http.StatusBadRequest)
		return
	}
	// в нашем случае q примет значение "something"
	// продолжаем обработку запроса
	// ...
}
