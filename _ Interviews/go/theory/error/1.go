package main

import (
	"log"
)

type customError struct{}

func (c *customError) Error() string {
	return "Find the bug."
}

func fail() ([]byte, *customError) {
	return nil, nil
}

func main() {
	var err error
	if _, err = fail(); err != nil {
		log.Fatal("Why did this fail?")
	}
	log.Println("No Error")
}
