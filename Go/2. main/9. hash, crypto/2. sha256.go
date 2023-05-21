package main

import (
	"crypto/sha256"
	"fmt"
)

/*
В этом уроке разберём криптографические хеш-функции.
В Go есть общий для всех хеш-функций интерфейс — hash.Hash.
Вычислим хеш-функцию SHA256. Реализация этой хеш-функции — в пакете crypto/sha256.
*/

func main() {
	src := []byte("Здесь могло быть написано, чем Go лучше Rust. " +
		"Но после хеширования уже не прочитаешь.")

	hasher := sha256.New()
	hasher.Write(src)
	dst := hasher.Sum(nil)
	fmt.Printf("%x", dst)

	// or
	fmt.Printf("\n%x", sha256.Sum256(src))
}
