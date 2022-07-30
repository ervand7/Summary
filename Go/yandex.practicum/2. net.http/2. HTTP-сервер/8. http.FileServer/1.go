package main

import (
	"log"
	"net/http"
)

func main() {
	// конструируем Handler
	// в качестве файловой системы передаём нативную ФС сервера,
	// ограниченную директорией ./assets
	fs := http.FileServer(http.Dir("./assets"))
	// регистрируем URL /static и перенаправляем хендлеру
	// функция StripPrefix убирает из URL запроса префикс static
	// запрос domain.com/static/path/file.html будет открывать файл path/file.html
	// файловой системы сервера с корнем ./assets
	http.Handle("/static/", http.StripPrefix("/static/", fs))
	err := http.ListenAndServe(":6000", nil)
	if err != nil {
		log.Fatal(err)
	}
}
