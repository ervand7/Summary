package main

import (
	"compress/gzip"
	"fmt"
	"io"
	"net/http"
)

/*
Измените обработчик LengthHandle так, чтобы он распаковывал тело запроса
только при наличии заголовка Content-Encoding: gzip. Если заголовка нет,
должен возвращаться размер тела запроса без декомпрессии.
*/

func LengthHandle_(w http.ResponseWriter, r *http.Request) {
	// переменная reader будет равна r.Body или *gzip.Reader
	var reader io.Reader

	if r.Header.Get(`Content-Encoding`) == `gzip` {
		gz, err := gzip.NewReader(r.Body)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		reader = gz
		defer gz.Close()
	} else {
		reader = r.Body
	}

	body, err := io.ReadAll(reader)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	fmt.Fprintf(w, "Length: %d", len(body))
}
