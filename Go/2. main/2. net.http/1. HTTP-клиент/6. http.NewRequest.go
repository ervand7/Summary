package main

import (
	"fmt"
	"net/http"
	"net/http/httputil"
)

func main() {
	// http.Request в отличие от http.Client не подходит для многопоточного
	// использования. Каждый раз нужно создавать новый запрос.
	/*
		Последний аргумент в вызове — body запроса типа io.Reader.
		Поскольку GET-запрос может не иметь тела, здесь допустимо nil.
	*/
	request, err := http.NewRequest(
		http.MethodGet, "http://127.0.0.1:8000/api/v1/feedbacks_list/", nil)
	if err != nil {
		// обработаем ошибку
	}

	/*
		Поле request.Header содержит заголовки запроса — пары «ключ-значение»
		в формате map[string][]string.
		Добавим заголовок. Обращаемся к REST API и ожидаем ответ в формате JSON:
	*/
	request.Header.Set("Content-Type", "application/json; charset=UTF-8")
	request.Header.Add("Accept", "application/json")

	requestDump, err := httputil.DumpRequest(request, true)
	if err != nil {
		fmt.Println(err.Error())
	}
	fmt.Println(string(requestDump))
}

/*
GET /api/v1/feedbacks_list/ HTTP/1.1
Host: 127.0.0.1:8000
Accept: application/json
Content-Type: application/json; charset=UTF-8
*/
