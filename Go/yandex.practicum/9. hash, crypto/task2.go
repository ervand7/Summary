package main

import (
	"bytes"
	"crypto/md5"
	"crypto/rand"
	"fmt"
)

/*
Допишите программу, которая считает хеш MD5 случайной последовательности
512 байт. Один подсчёт сделайте с использованием интерфейса hash.Hash,
а другой — функцией md5.Sum([]byte).
*/

func main() {
	var (
		data  []byte
		hash1 []byte
		hash2 [md5.Size]byte
	)
	data = make([]byte, 512)
	_, err := rand.Read(data)
	if err != nil {
		panic(err)
	}

	hasher := md5.New()
	hasher.Write(data)
	hash1 = hasher.Sum(nil)

	hash2 = md5.Sum(data)

	if bytes.Equal(hash1, hash2[:]) { // hash2[:] приводит массив байт к слайсу
		fmt.Println("Всё правильно! Хеши равны")
	} else {
		fmt.Println("Что-то пошло не так")
	}
}
