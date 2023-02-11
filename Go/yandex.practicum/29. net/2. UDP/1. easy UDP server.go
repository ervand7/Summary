package main

import (
	"fmt"
	"net"
)

func main() {
	// слушаем порт 8080
	socket, err := net.ListenUDP("udp4", &net.UDPAddr{
		IP:   net.IPv4(0, 0, 0, 0),
		Port: 8080,
	})
	if err != nil {
		fmt.Println("listening failed!", err)
		return
	}
	// не забываем закрыть
	defer socket.Close()
	for {
		// аллокация буфера
		data := make([]byte, 4096)
		// читаем пришедший пакет в буфер
		read, remoteAddr, err := socket.ReadFromUDP(data)
		if err != nil {
			fmt.Println("read data failed!", err)
			continue
		}
		fmt.Println(read, remoteAddr)
		fmt.Printf("%s\n\n", data)
		// отправляем ответ
		sendData := []byte("Hello, client!")
		_, err = socket.WriteToUDP(sendData, remoteAddr)
		if err != nil {
			fmt.Println("send data failed!", err)
			return
		}
	}
}
