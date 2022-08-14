package main

import (
	"github.com/go-chi/chi/v5"
	"log"
	"net/http"
)

func NewRouter() chi.Router {
	r := chi.NewRouter()

	r.Route("/cars", func(r chi.Router) {
		r.Get("/{brand}", func(w http.ResponseWriter, r *http.Request) {
			brand := chi.URLParam(r, "brand")
			w.Write([]byte("brand:" + brand))
		})
		r.Get("/{brand}/{model}", func(w http.ResponseWriter, r *http.Request) {
			brand := chi.URLParam(r, "brand")
			model := chi.URLParam(r, "model")
			w.Write([]byte("brand and model:" + brand + "-" + model))
		})
	})
	return r
}

func main() {
	log.Fatal(http.ListenAndServe(":8080", NewRouter()))
}
