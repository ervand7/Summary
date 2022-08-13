package main

import "net/http"

type ApiHandler struct {
	Templ []byte
}

func (a ApiHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Write(a.Templ)
}

/*
Например, чтобы зарегистрировать совпадение обработчика ApiHandler
со всеми URL, которые начинаются с /api/, можно написать:
*/
func main() {
	var handler ApiHandler
	mux := http.NewServeMux()
	mux.Handle("/api/", handler)

	/*
		Или, если по умолчанию используем DefaultServeMux, проще сделать так:
		http.Handle("/api/", handler3)

		Обработчик ищет паттерн по совпадению строки максимальной длины.
		Если зарегистрировать
		http.Handle("/api/", apiHandler)
		http.Handle("/api/auth", apiAuthHandler)
		и запросить domain.com/api/auth, будет вызван apiAuthHandler.
		Если паттерн /api/auth не зарегистрирован, обработка будет передана apiHandler.
	*/
}
