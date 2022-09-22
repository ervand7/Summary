package main

import (
	"fmt"
	"runtime"
	"time"
)

func main() {
	runtime.GOMAXPROCS(1)
	go func() {
		var u int
		for {
			u -= 2

			if u == 1 {
				fmt.Print(u)
				break
			}
		}
	}()
	<-time.After(time.Millisecond * 5) // в этом месте main горутина разбудит планировщик, а он в свою очередь запустит горутину с циклом

	fmt.Println("go 1.13 has never been here")
}
