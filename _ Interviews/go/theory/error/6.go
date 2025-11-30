package main

import (
	"fmt"
)

type calcError struct {
	msg string
}

func (c *calcError) Error() string { return c.msg }

func compute(x int) *calcError {
	if x < 0 {
		return &calcError{"negative input"}
	}

	return nil
}

func main() {
	var err error

	if err = compute(10); err != nil {
		fmt.Println("ERROR:", err)
	} else {
		fmt.Println("NO ERROR")
	}
}
