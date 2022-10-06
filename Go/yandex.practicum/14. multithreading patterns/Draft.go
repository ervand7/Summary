package main

import "fmt"

func main() {
	type d struct{ qwe string }
	//type d struct{qwe string}{qwe: asd}
	a := struct{}{}
	fmt.Println(a)
}
