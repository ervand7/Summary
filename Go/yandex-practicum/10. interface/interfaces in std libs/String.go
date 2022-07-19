package main

import (
	"fmt"
	"time"
)

type User struct {
	Email        string
	PasswordHash string
	LastAccess   time.Time
}

func (u User) String() string {
	return "user with email " + u.Email
}

func main() {
	u := User{Email: "example@yandex.ru"}
	fmt.Printf("Hello, %s", u) // Hello, user with email example@yandex.ru
}
