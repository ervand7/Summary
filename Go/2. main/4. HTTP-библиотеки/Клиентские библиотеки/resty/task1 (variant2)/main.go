package main

import (
	"errors"
	"fmt"
	"github.com/go-resty/resty/v2"
	"log"
	"net/http"
	"sort"
	"time"
)

// User — структура объекта.
// Обратите внимание на описание полей внутри структуры.
type User struct {
	ID       int    `json:"id"`
	Name     string `json:"name"`
	Username string `json:"username"`
	Email    string `json:"email"`
	Phone    string `json:"phone"`
	Website  string `json:"website"`

	Address struct {
		Street  string `json:"street"`
		Suite   string `json:"suite"`
		City    string `json:"city"`
		Zipcode string `json:"zipcode"`
		Geo     struct {
			Lat string `json:"lat"`
			Lng string `json:"lng"`
		} `json:"geo"`
	} `json:"address"`

	Company struct {
		Name        string `json:"name"`
		CatchPhrase string `json:"catchPhrase"`
		Bs          string `json:"bs"`
	} `json:"company"`
}

func main() {
	client :=
		resty.New().
			SetHostURL("https://jsonplaceholder.typicode.com/").
			SetRetryCount(5).
			SetRetryWaitTime(10 * time.Second).
			SetRetryMaxWaitTime(20 * time.Second)
	users, err := getUsers(client)
	if err != nil {
		log.Panic(err)
	}

	sortUser(users)

	for _, u := range users {
		fmt.Println(u.Name)
	}
}

// getUsers возвращает пользователей.
func getUsers(client *resty.Client) ([]User, error) {
	var users []User

	// обратите внимание, что в этой части кода используется
	// встроенная в resty функция SetResult,
	// она позволяет избежать работы с чтением ответа и обязательной
	// проверки на ошибки,
	// Resty сделает это автоматически
	resp, err := client.R().SetResult(&users).Get("/users")
	if err != nil {
		return nil, err
	}

	if resp.StatusCode() != http.StatusOK {
		return nil, errors.New("can't get users. Status code <> 200")
	}

	return users, nil
}

// sortUser сортирует по имени.
func sortUser(users []User) {
	sort.Slice(users, func(i, j int) bool {
		return users[i].Name < users[j].Name
	})
}
