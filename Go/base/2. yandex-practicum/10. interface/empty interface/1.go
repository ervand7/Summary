package main

import (
	"fmt"
	"strconv"
)

func Printf(v interface{}) {

	switch value := v.(type) {
	case int64:
		fmt.Print("\nЭто число " + strconv.FormatInt(value, 10))
	case string:
		fmt.Print("\nЭто строка " + value)
	default:
		fmt.Print("\nНеизвестный тип")
	}
}
func main() {
	mySlice := make([]int, 0)

	Printf(int64(3)) // Это число 3
	Printf("Hello")  // Это строка Hello
	Printf(mySlice)  // Неизвестный тип
}
