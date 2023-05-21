package main

import (
	"flag"
	"fmt"
)

// Декларации флагов можно помещать в init()-функциях пакета:

var (
	host *string
	port *int
)

func init() {
	host = flag.String("host", "localhost", "Domain name")
	port = flag.Int("port", 8080, "port number")
}

/*
Тогда в main() останется только сделать flag.Parse().
Вызывать flag.Parse() в init()-функциях не следует, потому что
порядок выполнения этих функций трудно предсказать.
*/
func main() {
	flag.Parse()
	fmt.Println(*host)
	fmt.Println(*port)
}

/*
$ go run 5.\ Использование\ init-функций.go --host=129.3.554.3.11 --port=5000
129.3.554.3.11
5000
*/
