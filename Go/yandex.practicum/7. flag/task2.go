package main

import (
	"flag"
	"fmt"
	"os"
)

/*
Функция flag.Usage объявлена в пакете как переменная, то есть можно её модифицировать.
Напишите собственную функцию, которая, кроме имени, будет выводить релиз/версию утилиты
*/

var version = "0.0.1"

func main() {
	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(), "Usage of %s:\nVersion%s:\n", os.Args[0], version)
		flag.PrintDefaults()
	}

	flag.Parse()
}

/*
$ go run task2.go --help
Usage of /var/folders/ky/889zsrl12nvcz0x0wdr24hsm0000gn/T/go-build4206051006/b001/exe/task2:
Version0.0.1:
*/
