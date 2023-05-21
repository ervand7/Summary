package main

import (
	"fmt"
	"time"
)

func main() {
	var date int
	fmt.Scan(&date)

	switch {
	case date >= 1946 && date <= 1964:
		fmt.Println("Привет, бумер!")

	case date >= 1965 && date <= 1980:
		fmt.Println("Привет, представитель X!")

	case date >= 1981 && date <= 1996:
		fmt.Println("Привет, миллениал X!")

	case date >= 1997 && date <= 2012:
		fmt.Println("Привет, зумер X!")

	case date >= 2013 && date <= time.Now().Year():
		fmt.Println("Привет, альфа X!")
	}
}
