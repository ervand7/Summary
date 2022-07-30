package main

import (
	"log"
	"net/http"
)

/*
Например, функцию
func Redirect(w ResponseWriter, r *Request, url string, code int)
можно использовать так:
*/

func redirect(w http.ResponseWriter, r *http.Request) {
	http.Redirect(w, r, "https://yandex.ru/", http.StatusMovedPermanently)
}

func main() {
	http.HandleFunc("/search/", redirect)
	log.Fatal(http.ListenAndServe(":8080", nil))

	/*
		Функции-генераторы
		http.NotFoundHandler(),
		http.RedirectHandler(),
		http.TimeoutHandler()
		использовать ещё проще, потому что они возвращают готовый http.Handler:
		http.Handle("/dummy", http.RedirectHandler("https://google/com", 301))
	*/
}
