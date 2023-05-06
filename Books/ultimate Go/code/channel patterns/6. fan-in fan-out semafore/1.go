package main

import (
	"fmt"
	"time"
)

func main() {
	children := 100
	ch := make(chan string, children)
	g := 10
	sem := make(chan bool, g)

	for i := 0; i < children; i++ {
		go func(i int) {
			// Этим каналом мы контролируем, что одновременно работают только
			// 10 горутин. Несмотря на то, что создано для одновременной 100 штук
			sem <- true
			{
				time.Sleep(time.Second)
				ch <- "data"
				fmt.Println("child : sent signal :", i)
			}
			<-sem
		}(i)
	}
	for children > 0 {
		<-ch
		children--
		fmt.Println("parent : recv'd signal :", children)
	}
	time.Sleep(time.Second)
	fmt.Println("-------------------------------------------------")
}
