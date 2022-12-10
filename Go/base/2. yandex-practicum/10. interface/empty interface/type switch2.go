package main

import (
	"fmt"
	"strings"
)

func Mul(a interface{}, b int) interface{} {
	switch value := a.(type) {
	case int:
		return value * b
	case string:
		return strings.Repeat(value, b)
	default:
		return nil
	}
}
func main() {
	fmt.Println(Mul("Hello", 7)) // HelloHelloHelloHelloHelloHelloHello
	fmt.Println(Mul(7, 7))       // 49
	fmt.Println(Mul(1.2, 7))     // <nil>
}
