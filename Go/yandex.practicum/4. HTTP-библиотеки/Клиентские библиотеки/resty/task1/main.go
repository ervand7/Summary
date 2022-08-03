package main

import (
	"fmt"
	"github.com/go-resty/resty/v2"
	"sort"
	"time"
)

/*
Сделайте запросы к API: https://jsonplaceholder.typicode.com/.
Приложение должно уметь:
	Выводить всех пользователей /users/ в
	виде JSON: GET https://jsonplaceholder.typicode.com/users.

	Выводить пользователей в отсортированном виде по полю name,
	а не по id. Для этого сделайте сортировку внутри приложения.

	В случае ошибки от сервера повторять запрос 5 раз с
	интервалом 10 секунд. После пятого неуспешного запроса выводить
	в консоль сообщение о невозможности сделать запрос.
*/

type (
	User struct {
		ID       int     `json:"id"`
		Name     string  `json:"name"`
		Username string  `json:"username"`
		Email    string  `json:"email"`
		Address  Address `json:"address"`
		Phone    string  `json:"phone"`
		Website  string  `json:"website"`
		Company  Company `json:"company"`
	}

	Address struct {
		Street  string `json:"street"`
		Suite   string `json:"suite"`
		City    string `json:"city"`
		Zipcode string `json:"zipcode"`
	}

	Company struct {
		Name        string `json:"name"`
		CatchPhrase string `json:"catchPhrase"`
		Bs          string `json:"bs"`
	}
)

func main() {
	var users []User
	url := "https://jsonplaceholder.typicode.com/users"
	client := resty.New()
	client.
		SetRetryCount(5).
		SetRetryWaitTime(10 * time.Second)

	usersJson, err := client.R().
		SetResult(&users).
		Get(url)

	if err != nil {
		fmt.Printf("unable to make request: %s", err)
	}

	fmt.Println(usersJson)

	sort.Slice(users, func(i, j int) bool {
		return users[i].Name < users[j].Name
	})
	for _, u := range users {
		fmt.Println(u.Name)
	}
}
