package main

import (
	"fmt"
	"io"
	"net/http"
)

func main() {
	response, err := http.Get("http://127.0.0.1:8000/api/v1/feedbacks_list/")
	if err != nil {
		fmt.Println(err)
	}
	/*
		Тело ответа response.Body представлено интерфейсом потокового
		чтения io.ReadCloser. Иногда проще и удобнее применить к response.Body
		функцию io.ReadAll(). И важно не забыть закрыть его после чтения.
	*/
	defer response.Body.Close()
	payload, err := io.ReadAll(response.Body)
	fmt.Println(string(payload))
}

// {"count":1, "next":null, "previous":null, "results":[{"id":1, "time_create":"2022-06-05T13:02:49.415000Z", "time_update":"2022-06-05T13:02:49.415000Z", "description":"qweqw", "category":"Other","age_confirmation":true, "content":"qwe", "user":1}]}
