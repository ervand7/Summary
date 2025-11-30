package main

import (
	"errors"
	"fmt"
)

// unexpected behaviour because we use direct comparison instead of errors.Is

var ErrNotFound = errors.New("not found")

func load(flag bool) error {
	if flag {
		return fmt.Errorf("wrapper: %w", ErrNotFound)
	}
	return nil
}

func main() {
	err := load(true)

	if err == ErrNotFound {
		fmt.Println("ErrNotFound matched")
	} else {
		fmt.Println("No match")
	}
}
