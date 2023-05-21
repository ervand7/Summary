package main

import (
	"flag"
	"fmt"
)

func main() {
	wordPtr := flag.String("word", "foo", "a string")
	flag.Parse()
	fmt.Println("word:", *wordPtr) // word: foo
}

/*
1) $ go run 1.\ Пример\ минимального\ кода.go --help
Usage of /var/folders/ky/889zsrl12nvcz0x0wdr24hsm0000gn/T/go-build2276462596/b001/exe/1. Пример минимального кода:
  -word string
        a string (default "foo")

2) go run 1.\ Пример\ минимального\ кода.go --word HelloWorld!
word: HelloWorld!
*/
