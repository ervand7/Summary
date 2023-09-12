package main

import (
	"fmt"
	"runtime"
	"time"
)

/*
Но с обычным GOMAXPROCS (=8) бесконтрольная горутина отработает только
time.Millisecond, а далее произойдет выход из горутины, так как произойдет
выход из всей программы.
*/

func main() {
	runtime.GOMAXPROCS(8)
	go func() {
		for true {
			fmt.Println("Infinite loop")
		}
	}()

	time.Sleep(time.Millisecond)
	fmt.Println("finish")
}
