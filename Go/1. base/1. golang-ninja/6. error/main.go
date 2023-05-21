package main

import (
	"errors"
	"fmt"
	"log"
)

func main() {
	message, err := enterTheClub(55)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(message)
}

func enterTheClub(age int) (string, error) {
	if age >= 18 && age < 45 {
		return "Входи", nil
	} else if age >= 45 && age < 65 {
		return "Вам точно понравится эта музыка?", nil
	} else if age >= 65 {
		return "Это уже слишком для вас", errors.New("you are too old")
	}

	return "Тебе нет 18", errors.New("you are too yang")
}
