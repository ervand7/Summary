package main

import (
	"github.com/go-chi/chi/v5"
	"net/http"
)

func main() {
	r := chi.NewRouter()
	r.Get("/", func(rw http.ResponseWriter, r *http.Request) {
		rw.Write([]byte("chi"))
	})
	http.ListenAndServe(":8080", r)
}
