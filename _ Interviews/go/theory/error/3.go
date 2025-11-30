package main

import (
	"fmt"
)

/*
Now we receive `ERROR: boom`.
To have predictable behaviour, we should use `var err error` instead of `var e *myErr`.
*/

type myErr struct{}

func (m *myErr) Error() string { return "boom" }

func maybeError(flag bool) error {
	var e *myErr
	if flag {
		e = &myErr{}
	}
	return e
}

func main() {
	err := maybeError(false)

	if err != nil {
		fmt.Println("ERROR:", err)
	} else {
		fmt.Println("NO ERROR")
	}
}
