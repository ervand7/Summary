package main

import (
	"flag"
	"fmt"
	"strings"
)

// Например, утилита, принимающая флаг -users=John,Mary,Ivan,qweqwe,
// может содержать такой код:

func main() {
	// готовим переменную для аргументов
	var users []string
	// декларируем функцию-обработчик
	flag.Func("users", "List of users", func(flagValue string) error {
		// разбиваем значение флага на слайс строк через запятую и заливаем в переменную
		users = strings.Split(flagValue, ",")
		fmt.Println(users)
		return nil
	})
	// запускаем парсинг
	flag.Parse()
}

/*
$ go run 8.\ flag.Func\(\)\ —\ пользовательские\ правила\ обработки.go -users=John,Mary,Ivan,qweqwe
[John Mary Ivan qweqwe]
*/
