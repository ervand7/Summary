package main

import (
	"context"
	"fmt"
	"net/http"
	"time"
)

func main() {
	/*
		Нужно понимать, что Да. client.Timeout действует в рамках клиента,
		а request.Context, приведенный в этом примере, — в рамках запроса.
		Например, чтобы ограничить время ожидания запроса одной
		секундой, можно написать:
	*/
	// конструируем контекст с Timeout
	ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
	// функция cancel() позволяет при необходимости остановить операции
	defer cancel()
	// собираем запрос с контекстом
	req, _ := http.NewRequestWithContext(
		ctx,
		"GET",
		"http://127.0.0.1:8000/api/v1/feedbacks_list/",
		nil,
	)
	// конструируем клиент
	client := &http.Client{}
	// отправляем запрос
	resp, err := client.Do(req)
	fmt.Println(resp, err)
}
