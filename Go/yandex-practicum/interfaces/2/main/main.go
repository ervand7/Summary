package main

import (
	"fmt"
	"randbyte"
	"time"
)

func main() {
	param := time.Now().UnixNano()
	generator := randbyte.New(param)
	buf := make([]byte, 16)
	for i := 0; i < 5; i++ {
		n, _ := generator.Read(buf)
		fmt.Printf("Generate bytes: %v size(%d)\n", buf, n)
	}
}
