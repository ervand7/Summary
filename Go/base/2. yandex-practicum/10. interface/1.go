package main

import (
	"fmt"
	"time"
)

type User struct {
	Email      string
	Password   string
	LastAccess time.Time
}

func (u User) String() string {
	return "user with email " + u.Email
}

func Printf(v fmt.Stringer) {
	fmt.Print("Это тип, реализующий Stringer, " + v.String())
}

func main() {
	u := User{Email: "example@yandex.ru"}
	Printf(u)
}
