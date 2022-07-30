package main

import (
	"fmt"
	"net/http"
)

func main() {
	client := http.Client{}
	response, err := client.Get("http://127.0.0.1:8000/api/v1/feedbacks_list/")
	fmt.Println(response, err)
}
