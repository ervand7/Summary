package main

import "fmt"

// Можно вызвать метод инстанса и через тип

type user struct {
	name    string
	surname string
}

func (u user) methWitValue() {
	fmt.Println(u.name, u.surname)
}

func (u *user) methWitPointer() {
	fmt.Println(u.name, u.surname)
}

func main() {
	u := user{name: "qwe", surname: "asd"}
	user.methWitValue(u)       // qwe asd
	(*user).methWitPointer(&u) // qwe asd
}
