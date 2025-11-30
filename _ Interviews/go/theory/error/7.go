package main

import (
	"errors"
	"fmt"
)

func process(flag bool) (err error) {
	if flag {
		err := errors.New("something went wrong")
		return err
	}

	return nil
}

func main() {
	err := process(true)

	if err != nil {
		fmt.Println("ERROR:", err)
	} else {
		fmt.Println("NO ERROR")
	}
}
