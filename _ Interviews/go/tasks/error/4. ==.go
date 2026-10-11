package main

import (
	"errors"
	"fmt"
)

type MyErr struct {
	Data string
}

func (e *MyErr) Error() string {
	return fmt.Sprintf("my error: %s", e.Data)
}

func main() {
	var err1 error = &MyErr{Data: "hello"}
	var err2 error

	fmt.Println(err1 == err2)

	fmt.Println(errors.As(err1, &err2))
	fmt.Println(err1 == err2)
}
