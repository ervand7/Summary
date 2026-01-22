package main

import (
	"errors"
	"fmt"
)

type myError struct{}

func (e *myError) Error() string {
	return "boom"
}

func returnsError() error {
	var e *myError = nil
	return e
}

func main() {
	err := returnsError()

	fmt.Println(err == nil)
	fmt.Println(errors.Is(err, nil))

	var target *myError
	fmt.Println(errors.As(err, &target))
	fmt.Println(target == nil)
}
