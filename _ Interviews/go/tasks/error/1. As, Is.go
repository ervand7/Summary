package main

import (
	"errors"
	"fmt"
)

type SomeError struct {
	Data string
}

func (e *SomeError) Error() string {
	return fmt.Sprintf("some error: %s", e.Data)
}

func handle() error {
	return &SomeError{
		Data: "data",
	}
}

func main() {
	err := handle()
	if errors.Is(err, &SomeError{}) {
		fmt.Println(1)
	}

	var typedErr error
	if errors.As(err, &typedErr) {
		fmt.Println(2)
	}
	fmt.Println(3)

	if errors.Is(err, typedErr) {
		fmt.Println(4)
	}
}
