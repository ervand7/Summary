package main

import (
	"crypto/rand"
	"encoding/base64"
	"fmt"
)

/*
Напишите функцию, которая будет генерировать массив случайных байт.
Размер массива передаётся параметром. Функция должна возвращать массив
в виде строки в кодировке base64. Используйте пакет encoding/base64.
*/

func main() {
	fmt.Println(RandBytes(19)) // SZed+Tfoh4CxS1B6tiyiCLBB5w== <nil>
}

func RandBytes(n int) (string, error) {
	b := make([]byte, n)
	_, err := rand.Read(b)
	if err != nil {
		return ``, err
	}
	return base64.StdEncoding.EncodeToString(b), nil
}
