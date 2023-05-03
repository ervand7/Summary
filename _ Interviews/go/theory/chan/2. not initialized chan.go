package main

import "fmt"

/*
Удивительно, но ошибка при использовании неинициализированного канала - deadlock
*/

func main() {
	var ch chan int

	go func() {
		ch <- 7
	}()
	v := <-ch
	fmt.Println(v)
}
