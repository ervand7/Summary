package main

import (
	"fmt"
	"net"
)

func main() {
	// открываем сокет
	socket, err := net.DialUDP("udp4", nil, &net.UDPAddr{
		IP:   net.IPv4(127, 0, 0, 1),
		Port: 8080,
	})
	if err != nil {
		fmt.Println("connection failed!", err)
		return
	}
	// сокет нужно будет закрыть
	defer socket.Close()
	sendData := []byte("hello server!")
	// отправляем данные
	_, err = socket.Write(sendData)
	if err != nil {
		fmt.Println("send data failed!", err)
		return
	}
	// аллокация буфера
	data := make([]byte, 4096)
	// читаем ответ в буфер
	read, remoteAddr, err := socket.ReadFromUDP(data)
	if err != nil {
		fmt.Println("read data failed!", err)
	}
	fmt.Println(read, remoteAddr)
	fmt.Printf("%s\n", data)
}
