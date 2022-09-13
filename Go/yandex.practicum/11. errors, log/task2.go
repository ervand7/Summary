package main

import (
	"bytes"
	"fmt"
	"log"
)

/*
Создайте переменную типа *log.Logger, которая будет использовать bytes.Buffer для
записи данных. В результате работы программы в буфере должно быть:

mylog: Hello, world!
mylog: Goodbye
*/

func main() {
	var buf bytes.Buffer
	// допишите код
	// 1) создайте переменную типа *log.Logger
	mylog := log.New(&buf, `mylog: `, 0)
	// 2) запишите в неё нужные строки
	mylog.Println("Hello, world!")
	mylog.Println("Goodbye")

	fmt.Print(&buf)
	// mylog: Hello, world!
	// mylog: Goodbye
}
