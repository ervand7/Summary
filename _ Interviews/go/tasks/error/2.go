package main

import (
	"errors"
	"fmt"
)

type MyError struct {
	Code int
}

func (e MyError) Error() string {
	return fmt.Sprintf("code=%d", e.Code)
}

func main() {
	base := MyError{Code: 404}
	wrapped := fmt.Errorf("wrapped: %w", base)

	fmt.Println(errors.Is(wrapped, MyError{}))
	fmt.Println(errors.Is(wrapped, &MyError{}))

	var e MyError
	fmt.Println(errors.As(wrapped, &e))
	fmt.Println(e.Code)
}
