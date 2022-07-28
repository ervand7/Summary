package main

import (
	"fmt"
	"time"
)

// Обрежьте время до текущего дня, используя метод Truncate:
func main() {
	now := time.Now()
	truncTime := now.Truncate(time.Hour * 24)
	fmt.Println(truncTime)
}
