package main

import (
	"fmt"
	"github.com/asaskevich/govalidator"
	"log"
)

type Example struct {
	Name  string `valid:"-"`
	Email string `valid:"email"`
	URL   string `valid:"url"`
}

func main() {
	// проверяем на валидность email и URL
	result, err := govalidator.ValidateStruct(Example{
		Email: "johndoe@example.com",
		URL:   "https://www.ya.ru",
	})
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(result) // true
}
