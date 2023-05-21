package main

import (
	"fmt"
	"os"
)

func main() {
	args := os.Args
	fmt.Printf("All arguments: %v\n", args)
	// первый аргумент в списке — традиционно имя команды
	command := os.Args[0]
	fmt.Printf("Command name: %v\n", command)
	// далее слайс аргументов
	parameters := os.Args[1:]
	fmt.Printf("Parameters: %v\n", parameters)
}

/*
$ go run 2.\ os.Args.go qwe asd zxc
All arguments: [/var/folders/ky/889zsrl12nvcz0x0wdr24hsm0000gn/T/go-build3143485908/b001/exe/2. os.Args qwe asd zxc]
Command name: /var/folders/ky/889zsrl12nvcz0x0wdr24hsm0000gn/T/go-build3143485908/b001/exe/2. os.Args
Parameters: [qwe asd zxc]
*/
