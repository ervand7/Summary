package main

import (
	"flag"
	"fmt"
	"strings"
)

type Users struct {
	group string
	users []string
}

/*
нужно сделать парсинг флага вида -users=John,Mary,Ivan,qweqwe в
переменную такого типа. Для типа должен быть реализован интерфейс flag.Value:
type Value interface {
	String() string
	Set(string) error
}
*/

// String должен уметь сериализовать переменную типа в строку.
func (u *Users) String() string {
	return fmt.Sprint(strings.Join(u.users, ","))
}

// Set связывает переменную типа со значением флага
// и устанавливает правила парсинга для пользовательского типа.
func (u *Users) Set(flagValue string) error {
	u.users = strings.Split(flagValue, ",")
	return nil
}

// После этого можно сделать парсинг флага в пользовательский тип функцией flag.Var():
func main() {
	users := new(Users)
	// парсим значение флага users в переменную типа Users
	flag.Var(users, "users", "List of users")
	// запускаем парсинг
	flag.Parse()
	fmt.Printf("%#+v", users)
}

/*
go run 9.\ flag.Value\ —\ интерфейс\ пользовательской\ обработки.go -users=John,Mary,Ivan,qweqwe
&main.Users{group:"", users:[]string{"John", "Mary", "Ivan", "qweqwe"}}
*/
