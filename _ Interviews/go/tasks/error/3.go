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
	return e // returns a typed nil (*myError) stored in an interface -> interface != nil
}

func main() {
	err := returnsError()

	fmt.Println(err == nil)          // false: interface has type (*myError) even though value is nil
	fmt.Println(errors.Is(err, nil)) // false: Is checks error chain; typed nil != nil

	var target *myError
	fmt.Println(errors.As(err, &target)) // true: err has type *myError, so it matches
	fmt.Println(target == nil)           // true: underlying value is nil
}
