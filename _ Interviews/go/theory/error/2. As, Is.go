package main

import (
	"errors"
	"fmt"
)

type MyError struct {
	Code string `json:"code,omitempty"`
}

func (se MyError) Error() string {
	return fmt.Sprintf("Error detected: %s", se.Code)
}

func HandleError(code string) *MyError {
	return &MyError{
		Code: code,
	}
}

func some(err error, msg string) error {
	return fmt.Errorf("%s: %w", msg, err)
}

func main() {
	a := HandleError("Hello")
	b := some(a, "first")
	c := some(b, "second")
	d := some(c, "third")
	fmt.Println(d) // third: second: first: Error detected: Hello
	var e *MyError
	if errors.As(a, &e) && errors.As(b, &e) && errors.As(c, &e) && errors.As(d, &e) {
		fmt.Println(e) // Error detected: Hello
	}

	if errors.Is(d, a) && errors.Is(d, b) && errors.Is(d, c) {
		fmt.Println("Is!!!") // Is!!!
	}
}