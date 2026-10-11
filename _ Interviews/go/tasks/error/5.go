package main

import (
	"errors"
	"fmt"
)

type customErr struct {
	code int
}

func (e *customErr) Error() string {
	return "boom"
}

func returnErr() error {
	var err *customErr
	return err
}

func main() {
	var err *customErr
	fmt.Println(err == nil)

	returned := returnErr()
	fmt.Println(returned == nil)

	var custErr *customErr
	if errors.As(returned, &err) {
		fmt.Println(custErr.code)
	}
}
