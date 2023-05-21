package main

import (
	"errors"
	"flag"
	"fmt"
	"strconv"
	"strings"
)

/*
Реализуйте интерфейс flag.Value для типа NetAddress,
чтобы разобрать флаг --addr=example.com:60

Для решения этой задачи реализовываем интерфейс flag.Value
*/

type NetAddress struct {
	Host string
	Port int
}

func (n NetAddress) String() string {
	return n.Host + ":" + strconv.Itoa(n.Port)
}

func (n *NetAddress) Set(s string) error {
	splitParams := strings.Split(s, ":")
	if len(splitParams) != 2 {
		return errors.New("need address in n form host:port")
	}
	port, err := strconv.Atoi(splitParams[1])
	if err != nil {
		return err
	}
	n.Host = splitParams[0]
	n.Port = port
	return nil
}

func main() {
	addr := new(NetAddress)
	// проверка реализации
	flag.Var(addr, "addr", "Net address host:port")
	flag.Parse()
	fmt.Println(addr.Host)
	fmt.Println(addr.Port)
}

/*
$ go run task1.go --addr=example.com:60
example.com
60
*/
