package main

import "fmt"

/*
Ошибка при использовании неинициализированного канала - deadlock
*/

func main() {
	var ch chan int
	fmt.Println(ch == nil) // true

	go func() {
		ch <- 7
	}()
	v := <-ch
	fmt.Println(v)
}
