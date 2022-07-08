package main

import (
	"fmt"
)

// Base Enum implementation
type Base int

const (
	Info Base = iota + 1
	Warning
	Error
)

func main() {
	fmt.Println(Info, Warning, Error)
}
