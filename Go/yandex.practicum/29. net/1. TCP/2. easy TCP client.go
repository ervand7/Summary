package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	// устанавливаем соединение
	conn, err := net.Dial("tcp", "localhost:3333")
	if err != nil {
		fmt.Println(err)
		return
	}
	// буферизуем I/O
	req := bufio.NewReader(os.Stdin)
	resp := bufio.NewReader(conn)
	for {
		fmt.Print(">> ")
		text, err := req.ReadString('\n')
		if err != nil {
			fmt.Println("Error reading:", err)
			return
		}
		_, err = conn.Write([]byte(text + "\n"))
		if err != nil {
			fmt.Println("Error writing:", err)
			return
		}
		// читаем ответ сервера
		text, err = resp.ReadString('\n')
		if err != nil {
			fmt.Println("Error reading:", err)
			return
		}
		fmt.Println("<< " + text)
	}
}
