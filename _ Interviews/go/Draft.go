package main

import "fmt"

func main() {
	var ch = make(chan int)

	close(ch)
	close(ch)
	v := <-ch
	fmt.Println(v)
}
