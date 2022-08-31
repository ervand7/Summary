package main

import (
	"crypto/sha256"
	"fmt"
)

// Вычислим хеш-функцию SHA256

func main() {
	src := []byte("Здесь могло быть написано, чем Go лучше Rust. " +
		"Но после хеширования уже не прочитаешь.")

	h := sha256.New()
	h.Write(src)
	dst := h.Sum(nil)

	fmt.Printf("%x", dst)
}
