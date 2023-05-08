package main

import "fmt"

func service() {
	fmt.Println("Hello from service!")
}

func main() {
	// fmt.Println("main() started")

	// go service()

	select {}

	// fmt.Println("main() stopped")
}
