package main

import "log"

func main() {
	log.Print("Hello, world!")
	defer log.Fatal("Big problem!")
	log.Panic("Something goes wrong")
	log.Print("Success")
}

/*
2022/09/13 07:54:30 Hello, world!
2022/09/13 07:54:30 Something goes wrong
2022/09/13 07:54:30 Big problem!
*/
