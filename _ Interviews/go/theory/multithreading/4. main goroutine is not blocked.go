package main

import (
	"fmt"
)

/*
Поскольку хотя бы 1 горутина (в данном случае main) не заблокирована, то
дедлока не будет
*/

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
