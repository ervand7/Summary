package main

import (
	"fmt"
	"github.com/go-resty/resty/v2"
)

func main() {
	// создаём новый клиент
	client := resty.New()

	resp, err := client.R().
		SetAuthToken("Token 216421b8294c6066c3b9117b09f17af709df839b").
		Post("http://127.0.0.1:8000/api/v1/feedbacks_list/")

	fmt.Println("Исследуем объект Response:")
	fmt.Println("Error      :", err)
	fmt.Println("Status Code:", resp.StatusCode())
	fmt.Println("Status     :", resp.Status())
	fmt.Println("Time       :", resp.Time())
	fmt.Println("Received At:", resp.ReceivedAt())
	fmt.Println("Body       :\n", resp)
	fmt.Println("----")
}
