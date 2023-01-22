package main

import (
	"fmt"
	"log"
)

// defer will not be executed if there is a Fatal in the function

func main() {
	defer fmt.Println("Hello world")
	log.Fatal("Ooops")
}

// 2023/01/22 22:36:07 Ooops
