package main

import "fmt"

func AlignRight(s string, length int, lead rune) string {
	for len(s) < length {
		s = string(lead) + s
	}
	return s
}

func main() {

	fmt.Println("asd" + "sdf")
}
