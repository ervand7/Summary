package main

import "fmt"

func main() {
	defer printMessage() // this will be done before end of app
	fmt.Println("main")
	fmt.Println("main")
	fmt.Println("main")
}

func printMessage() {
	fmt.Println("printMessage")
}
