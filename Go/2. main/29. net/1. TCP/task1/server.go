package task1

import (
	"net"
)

const (
	Port   = ":52001" // порт сервера
	MaxLen = 1024     // максимальный размер слайса
)

// handleConn обрабатывает запросы и вычисляет среднее арифметическое.
func handleConn(c net.Conn) {
	// допишите код
	// ...
}

// TCPServer запускает сервер и ожидает соединений.
func TCPServer(addr *net.TCPAddr) {
	// допишите код
	// ...
}
