package main

import (
	"bytes"
	"net/http"
)

func main() {
	/*
		Передаём данные в формате JSON. В качестве io.Reader используем
		bytes.Buffer. В заголовках "Content-Type" устанавливаем "application/json".
		Так работают современные REST API.
	*/
	var body = []byte(`{"message":"Hello"}`)
	request, err := http.NewRequest(
		http.MethodPost,
		"http://127.0.0.1:8000/api/v1/feedbacks_list/",
		bytes.NewBuffer(body),
	)
	if err != nil {
		// обработаем ошибку
	}
	request.Header.Set("Content-Type", "application/json; charset=UTF-8")
}
