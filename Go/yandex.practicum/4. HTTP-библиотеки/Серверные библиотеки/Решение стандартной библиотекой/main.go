package main

import (
	"io"
	"log"
	"net/http"
	"strings"
)

/*
Представьте, что есть автосервис с интернет-магазином,
где продаются автомобили. Машин немного. В приложение
нужно добавить такие функции:
	показать определённую машину;
	показать все автомобили на одной странице.
Решить задачу можно с помощью пакета net/http в одном файле:
*/

var cars = map[string]string{
	"id1": "Renault",
	"id2": "BMW",
	"id3": "VW",
	"id4": "Audi",
}

func main() {
	// определяем хендлер, который выводит все машины
	http.HandleFunc("/cars", func(rw http.ResponseWriter, r *http.Request) {
		carsList := carsListFunc()
		_, err := io.WriteString(rw, strings.Join(carsList, ","))
		if err != nil {
			panic(err)
		}
	})

	// определяем хендлер, который выводит определённую машину
	http.HandleFunc("/car", func(rw http.ResponseWriter, r *http.Request) {
		carID := r.URL.Query().Get("id")
		if carID == "" {
			http.Error(rw, "carID param is missed", http.StatusBadRequest)
			return
		}
		rw.Write([]byte(carFunc(carID)))
	})

	log.Fatal(http.ListenAndServe(":8080", nil))
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
