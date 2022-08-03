package main

import (
	"fmt"
	"github.com/go-resty/resty/v2"
	"time"
)

/*
По адресу https://jsonplaceholder.typicode.com/posts/2 доступны след данные:
{
  "userId": 1,
  "id": 2,
  "title": "qui est esse",
  "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
}

Можно настроить автоматическую конвертацию ошибок и результата в объект —
методами SetError() и SetResult(). Например, так:
*/

// MyApiError — описание ошибки при неверном запросе.
type MyApiError struct {
	Code      int       `json:"code"`
	Message   string    `json:"message"`
	Timestamp time.Time `json:"timestamp"`
}

// Post — модель, описание основного объекта.
type Post struct {
	UserID int    `json:"userId"`
	ID     int    `json:"id"`
	Title  string `json:"title"`
	Text   string `json:"body"`
}

func main() {
	client := resty.New()

	var responseErr MyApiError
	var post Post

	_, err := client.R().
		SetError(&responseErr).
		SetResult(&post).
		Get("https://jsonplaceholder.typicode.com/posts/2")

	if err != nil {
		fmt.Println(responseErr)
		panic(err)
		return
	}

	fmt.Println(post)
}

/*
{1 2 qui est esse est rerum tempore vitae
sequi sint nihil reprehenderit dolor beatae ea dolores neque
fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis
qui aperiam non debitis possimus qui neque nisi nulla}
*/
