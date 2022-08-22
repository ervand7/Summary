package main

import (
	"errors"
	"flag"
	"fmt"
	"strconv"
	"strings"
)

/*
Реализуйте интерфейс flag.Value для типа
type NetAddress struct {
    Host string
    Port int

чтобы разобрать флаг --addr=example.com:60
}
*/

type NetAddress struct {
	Host string
	Port int
}

func (a NetAddress) String() string {
	return a.Host + ":" + strconv.Itoa(a.Port)
}

func (a *NetAddress) Set(s string) error {
	hp := strings.Split(s, ":")
	if len(hp) != 2 {
		return errors.New("need address in a form host:port")
	}
	port, err := strconv.Atoi(hp[1])
	if err != nil {
		return err
	}
	a.Host = hp[0]
	a.Port = port
	return nil
}

func main() {
	addr := new(NetAddress)
	// если интерфейс не реализован, здесь будет ошибка компиляции
	_ = flag.Value(addr)
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
