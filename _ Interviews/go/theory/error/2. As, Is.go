package main

import (
	"errors"
	"fmt"
)

type MyError struct {
	Code string `json:"code,omitempty"`
}

func (e MyError) Error() string {
	return fmt.Sprintf("Error detected: %s", e.Code)
}

func NewMyError(code string) *MyError {
	return &MyError{
		Code: code,
	}
}

func wrapErr(err error, msg string) error {
	return fmt.Errorf("%s: %w", msg, err)
}

func main() {
	a := NewMyError("Hello")
	b := wrapErr(a, "first")
	c := wrapErr(b, "second")
	d := wrapErr(c, "third")
	fmt.Println(d) // third: second: first: Error detected: Hello

	// Is сравнивает значение, возвращает true, если err == target, либо
	// err является дочерней ошибкой от target
	if errors.Is(d, a) && errors.Is(d, b) && errors.Is(d, c) {
		fmt.Println("Is!!!") // Is!!!
	}

	// As сравнивает тип, берет target и присваивает ему рутовою ошибку из err
	var e *MyError
	if errors.As(d, &e) && errors.As(c, &e) && errors.As(b, &e) && errors.As(a, &e) {
		fmt.Println(e) // Error detected: Hello
	}
}
