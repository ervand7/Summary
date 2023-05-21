package main

import (
	"bufio"
	"fmt"
	"net/rpc"
	"os"
)

func main() {
	// конструируем TCP-клиент
	client, err := rpc.Dial("tcp", "localhost:1234")
	if err != nil {
		fmt.Println(err)
	}
	// буферизуем ввод из консоли
	in := bufio.NewReader(os.Stdin)
	for {
		// читаем строку ввода
		line, _, err := in.ReadLine()
		if err != nil {
			fmt.Println(err)
		}
		var reply Reply
		// вызываем удалённый метод
		err = client.Call("Object.GetLine", line, &reply)
		if err != nil {
			fmt.Println(err)
		}
		// печатаем ответ, просто эхо
		fmt.Printf("Reply: %v, Data: %v", reply, reply.Data)
	}
}
