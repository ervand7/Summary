package main

import (
    "fmt"
    "log"
    "net"
    "net/rpc"
)

// Object — тип, методы которого будем экспортировать.
type Object int

// Reply — тип, в котором будем возвращать данные клиенту.
type Reply struct {
    Data string
}

// GetLine — экспортируемый метод.
func (o *Object) GetLine(line []byte, reply *Reply) error {
    rv := string(line)
    fmt.Printf("Receive: %v\n", rv)
    *reply = Reply{rv}
    return nil
}
func main() {
    // объявляем TCP-адрес на локальной машине, порт 1234
    addr, err := net.ResolveTCPAddr("tcp", "0.0.0.0:1234")
    if err != nil {
        log.Fatal(err)
    }
    // слушаем протокол TCP на объявленном адресе
    listener, err := net.ListenTCP("tcp", addr)
    if err != nil {
        log.Fatal(err)
    }
    // конструируем объект-экспортёр
    object := new(Object)
    // регистрируем экспорт
    rpc.Register(object)
    // обрабатываем входящее соединение
    rpc.Accept(listener)
}