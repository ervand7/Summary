package main

import (
	"fmt"
)

func main() {
	ch := make(chan int)
	for i := 0; i < 10; i++ {
		go func(num int) {
			fmt.Printf("goroutine %d waits...\n", num)
			val := <-ch
			fmt.Println(val)
		}(i)
	}

	fmt.Println("Ok")
}
