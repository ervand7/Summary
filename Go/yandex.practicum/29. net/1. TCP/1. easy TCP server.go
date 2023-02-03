package main

import (
	"fmt"
	"net"
	"os"
)

// handleConn обслуживает соединение.
func handleConn(conn net.Conn) {
	// не забываем освободить ресурсы
	defer conn.Close()
	// аллокация буфера для чтения из соединения
	b := make([]byte, 1024)
	// читаем из соединения в буфер
	for {
		_, err := conn.Read(b)
		if err != nil {
			fmt.Println("Error reading:", err)
			return
		}
		fmt.Println("Received message:", string(b))
		// отвечаем респонденту
		_, err = conn.Write([]byte("Got it. \n"))
		if err != nil {
			fmt.Println("Error writing:", err)
			return
		}
	}
}

func main() {
	// инициализируем TCP Listener
	l, err := net.Listen("tcp", "localhost:3333")
	if err != nil {
		fmt.Println("Error listening:", err)
		os.Exit(1)
	}
	// не забываем закрыть
	defer l.Close()
	for {
		// принимаем запросы на соединение
		conn, err := l.Accept()
		if err != nil {
			fmt.Println("Error accepting: ", err)
			continue
		}
		// обслуживаем соединение в горутине
		go handleConn(conn)
	}
}
