package task1

import (
	"math/rand"
	"net"
	"sync"
	"testing"
	"time"
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

func TestTCPServer(t *testing.T) {
	// запускаем и тестируем сервер
	addr, err := net.ResolveTCPAddr("tcp", Port)
	if err != nil {
		panic(err)
	}
	go TCPServer(addr)
	// ожидаем запуск сервера
	time.Sleep(100 * time.Millisecond)

	rand.Seed(time.Now().UnixNano())
	var wg sync.WaitGroup
	// тестируем на 5 соединениях с 50 запросами
	wg.Add(5)
	for j := 0; j < 5; j++ {
		go func() {
			c, err := net.DialTCP("tcp", nil, addr)
			if err != nil {
				t.Error(err)
			}
			for i := 0; i < 50; i++ {
				// размер данных должен быть > 0
				length := rand.Intn(MaxLen-1) + 1
				data := make([]byte, length)
				var sum int
				for k := 0; k < length; k++ {
					v := rand.Intn(256)
					data[k] = byte(v)
					sum += v
				}
				n, err := c.Write(data)
				if err != nil || n != length {
					t.Errorf("Write error n=%d length=%d err=%v ", n, length, err)
				}
				n, err = c.Read(data)
				if err != nil || n != 1 {
					t.Errorf("Read error n=%d err=%v ", n, err)
				}
				if data[0] != byte(sum/length) {
					t.Errorf("wrong average get %d - want %d", data[0], sum/length)
				}
			}
			wg.Done()
		}()
	}
	wg.Wait()
}
