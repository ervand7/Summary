package main

import (
	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"
	"io"
	"log"
	"net/http"
	"strings"
)

// Перепишите код из первого примера с машинами, используя роутер chi
var cars = map[string]string{
	"id1": "Renault",
	"id2": "BMW",
	"id3": "VW",
	"id4": "Audi",
}

func main() {
	// определяем роутер chi
	r := chi.NewRouter()
	// зададим встроенные middleware, чтобы улучшить стабильность приложения
	r.Use(middleware.RequestID)
	r.Use(middleware.RealIP)
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)

	r.Route("/cars", func(r chi.Router) {
		r.Get("/", func(rw http.ResponseWriter, r *http.Request) {
			carsList := carsListFunc()
			_, err := io.WriteString(rw, strings.Join(carsList, ","))
			if err != nil {
				panic(err)
			}
		})

		// создадим суброутер /{brand}, который будет содержать две функции
		r.Route("/{brand}", func(r chi.Router) {
			// /cars/{brand}
			r.Get("/", func(rw http.ResponseWriter, r *http.Request) {
				// код вывода всех автомобилей бренда
				brand := chi.URLParam(r, "brand")
				rw.Write([]byte(brand))
			})
			// /cars/{brand}/{model}
			r.Get("/{model}", func(rw http.ResponseWriter, r *http.Request) {
				// код вывода определённой модели
				// параметр brand будет доступен
				brand := chi.URLParam(r, "brand")
				model := chi.URLParam(r, "model")
				rw.Write([]byte(brand + " " + model))
			})
		})
	})

	log.Fatal(http.ListenAndServe(":8080", r))
}

// carsListFunc — вспомогательная функция для вывода всех машин.
func carsListFunc() []string {
	var list []string
	for _, c := range cars {
		list = append(list, c)
	}
	return list
}

// carFunc — вспомогательная функция для вывода определённой машины.
func carFunc(id string) string {
	if c, ok := cars[id]; ok {
		return c
	}
	return ""
}
