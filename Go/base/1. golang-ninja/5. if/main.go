package main

import "fmt"

func main() {
	message, entered := enterTheClub(57)
	fmt.Println(message, entered)
}

func enterTheClub(age int) (string, bool) {
	if age >= 18 && age < 45 {
		return "Входи", true
	} else if age >= 45 && age < 65 {
		return "Вам точно понравится эта музыка?", true
	} else if age >= 65 {
		return "Это уже слишком для вас", false
	}

	return "Тебе нет 18", false
}
