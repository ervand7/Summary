package main

import (
	"errors"
	"fmt"
)

type AppError struct {
	State int
}

func (c *AppError) Error() string {
	return fmt.Sprintf("App Error, State: %d", c.State)
}

func Cause(err error) error {
	root := err
	for {
		if err = errors.Unwrap(root); err == nil {
			return root
		}
		root = err
	}
}

func firstCall(i int) error {
	if err := secondCall(i); err != nil {
		return fmt.Errorf("secondCall(%d) : %w", i, err)
	}
	return nil
}

func secondCall(i int) error {
	return &AppError{99}
}

func main() {
	if err := firstCall(10); err != nil {
		var ap *AppError
		if errors.As(err, &ap) {
			fmt.Println("As says it is an AppError")
		}
		switch v := Cause(err).(type) {
		case *AppError:
			fmt.Println("Custom App Error:", v.State)
		default:
			fmt.Println("Default Error")
		}
		fmt.Printf("%v\n", err)
	}
}
