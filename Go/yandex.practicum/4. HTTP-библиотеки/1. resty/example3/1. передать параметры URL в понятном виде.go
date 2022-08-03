package main

import (
	"fmt"
	"github.com/go-resty/resty/v2"
)

func main() {
	client := resty.New()

	resp, err := client.R().SetPathParams(
		map[string]string{"postID": "1"},
	).Get("https://jsonplaceholder.typicode.com/posts/{postID}")

	if err != nil {
		panic(err)
	}

	fmt.Println(resp)
}

/*
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
*/
