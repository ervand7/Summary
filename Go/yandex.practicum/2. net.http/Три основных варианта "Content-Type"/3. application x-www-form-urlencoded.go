package main

import (
	"fmt"
	"net/http"
	"net/url"
	"strconv"
	"strings"
)

func main() {
	/*
		Это простой способ добавить к запросу данные в формате «ключ-значение».
		Данные могут быть помещены в query-строку
		URL — example.com/endpoint?key1=value1&key2=value2.
	*/

	// готовим контейнер для данных
	// используем тип url.Values из пакета net/url
	data := url.Values{}
	// устанавливаем данные
	data.Set("key1", "value1")
	data.Set("key2", "value2")
	// конструируем запрос
	request, err := http.NewRequest(
		"POST",
		"http://127.0.0.1:8000/api/v1/feedbacks_list/",
		strings.NewReader(data.Encode()),
	)
	if err != nil {
		// обработаем ошибку
	}
	// устанавливаем заголовки
	request.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	request.Header.Add("Content-Length", strconv.Itoa(len(data.Encode())))
	fmt.Println(request.Body)
}
