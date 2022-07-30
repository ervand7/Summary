package main

import (
	"errors"
	"fmt"
	"net/http"
	"time"
)

func main() {
	client := http.Client{}

	/*
		Теперь настроим клиент. Установим client.Timeout — максимальную задержку
		ответа, после которой клиент отменяет запрос. Значение этого параметра по
		умолчанию — 0. Клиент может ожидать ответа сколь угодно долго, но это
		блокирующая операция.
	*/
	client.Timeout = time.Second * 1

	response, err := client.Get("http://127.0.0.1:8000/api/v1/feedbacks_list/")
	fmt.Println(response, err)

	client.CheckRedirect = func(req *http.Request, via []*http.Request) error {
		if len(via) >= 2 {
			return errors.New("остановлено после двух Redirect")
		}
		return nil
	}
}
