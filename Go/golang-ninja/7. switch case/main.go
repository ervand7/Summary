package main

import (
	"errors"
	"fmt"
)

func main() {
	fmt.Println(prediction("чт"))
}

func prediction(dayOfWeek string) (string, error) {
	switch dayOfWeek {
	case "пн":
		return "Хорошего тебе начала недели", nil
	case "вт":
		return "Прекрасного тебе вторника", nil
	case "ср":
		return "Хорошей среды", nil
	case "чт":
		return "Четверг - это маленькая пятница", nil
	default:
		return "невалидный день недели", errors.New("invalid day of the week")
	}

}
