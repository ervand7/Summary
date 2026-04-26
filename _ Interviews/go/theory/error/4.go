package main

import (
	"errors"
	"fmt"
)

// we just overrode initial err

func doA() error {
	return errors.New("original failure")
}

func doB() error {
	if err := doA(); err != nil {
		err = fmt.Errorf("doB failed")
		return err
	}
	return nil
}

func main() {
	err := doB()
	if err != nil {
		fmt.Println("ERROR:", err)
	}
}
