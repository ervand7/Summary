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

func NewMyError(code string) *MyError {
	return &MyError{
		Code: code,
	}
}

func some(err error, msg string) error {
	return fmt.Errorf("%s: %w", msg, err)
}

func main() {
	a := NewMyError("Hello")
	b := some(a, "first")
	c := some(b, "second")
	d := some(c, "third")
	fmt.Println(d) // third: second: first: Error detected: Hello

	// Is сравнивает значение, возвращает true, если err == target, либо
	// err является дочерней ошибкой от target
	if errors.Is(d, a) && errors.Is(d, b) && errors.Is(d, c) {
		fmt.Println("Is!!!") // Is!!!
	}

	// As сравнивает тип, берет target и присваивает ему рутовою ошибку из err
	var e *MyError
	if errors.As(a, &e) && errors.As(b, &e) && errors.As(c, &e) && errors.As(d, &e) {
		fmt.Println(e) // Error detected: Hello
	}
}
