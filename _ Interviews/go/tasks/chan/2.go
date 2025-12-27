package main

import "fmt"

func main() {
	ch := make(chan string)
	go func() {
		for m := range ch {
			fmt.Printf("%s\n", m)
		}
	}()
	ch <- "cmd.1"
	ch <- "cmd.2"
}
