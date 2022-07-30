package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	/*
		client.Transport можно настраивать. Чтобы сэкономить ресурсы системы,
		можно уменьшить количество соединений, которые client.Transport кеширует и
		удерживает в состоянии idle.
	*/

	client := http.Client{}
	transport := &http.Transport{}
	transport.MaxIdleConns = 20
	client.Transport = transport

	response, error := client.Get("http://127.0.0.1:8000/api/v1/feedbacks_list/")
	fmt.Println(response, error)

	/*
		Чтобы повторно использовать кешированное TCP-соединение, клиент должен
		обязательно прочитать тело ответа до конца и закрыть, даже если оно не нужно.
	*/
	defer response.Body.Close()
	_, err := io.Copy(io.Discard, response.Body)
	if err != nil {
		fmt.Println(err)
	}
}
