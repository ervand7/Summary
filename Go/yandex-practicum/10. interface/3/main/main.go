package main

import (
	"fmt"
	"hashbyte"
)

func main() {
	buf := []byte{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
	hasher := hashbyte.New(-0)
	hasher.Write(buf)
	fmt.Printf("Hash: %v \n", hasher.Hash())
}
