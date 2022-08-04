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
	r := chi.NewRouter()
	// зададим встроенные middleware, чтобы улучшить стабильность приложения
	r.Use(middleware.RequestID)
	r.Use(middleware.RealIP)
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)

	/*
		// группируем все запросы /cars в одном месте
		r.Route("/cars", func(r chi.Router) {
			// GET /cars
			r.Get("/", getCars)
			// GET /cars/renault-logan
			r.Get("/{brand}-{model}", getCarByBrandAndModel)
			// GET /cars/renault-logan-2021-50000km-novaya
			r.Get("/{slug:[a-z-]+}", getCarBySlug)

			// создаём подроутер для /cars/{carID}
			r.Route("/{carID}", func(r chi.Router) {
				r.Get("/", getCar)       // GET /cars/1234
				r.Post("/", addCar)      // POST /cars/1234
				r.Delete("/", deleteCar) // DELETE /cars/1234
				r.Options("/", options)  // OPTIONS /cars/1234
			})
		})
	*/

	r.Get("/cars", func(rw http.ResponseWriter, r *http.Request) {
		carsList := carsListFunc()
		_, err := io.WriteString(rw, strings.Join(carsList, ","))
		if err != nil {
			panic(err)
		}
	})

	r.Get("/car", func(rw http.ResponseWriter, r *http.Request) {
		carID := r.URL.Query().Get("id")
		if carID == "" {
			http.Error(rw, "carID param is missed", http.StatusBadRequest)
			return
		}
		rw.Write([]byte(carFunc(carID)))
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
