package main

import (
	"net"
	"net/http"
)

// Можно запустить сервер со специфицированным net.Listener:
func main() {
	listener, err := net.Listen("tcp6", "[::1]:0")
	if err != nil {
		panic(err)
	}
	server := new(http.Server)
	err = server.Serve(listener)
	if err != nil {
		panic(err)
	}
}
