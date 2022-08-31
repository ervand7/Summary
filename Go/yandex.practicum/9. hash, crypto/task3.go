package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/binary"
	"encoding/hex"
	"fmt"
)

/*
Есть сообщение в 16-битном формате, состоящее из идентификатора uint32 и
подписи. Проверьте подпись алгоритмом HMAC, используя хеш-функцию SHA256 и
секретный ключ. Выведите значение идентификатора.
*/

var secretkey = []byte("secret key")

func main() {
	var (
		data []byte // декодированное сообщение с подписью
		id   uint32 // значение идентификатора
		err  error
		sign []byte // HMAC-подпись от идентификатора
	)
	msg := "048ff4ea240a9fdeac8f1422733e9f3b8b0291c969652225e25c5f0f9f8da654139c9e21"

	data, err = hex.DecodeString(msg)
	if err != nil {
		panic(err)
	}
	id = binary.BigEndian.Uint32(data[:4])
	h := hmac.New(sha256.New, secretkey)
	h.Write(data[:4])
	sign = h.Sum(nil)

	if hmac.Equal(sign, data[4:]) {
		fmt.Println("Подпись подлинная. ID:", id)
	} else {
		fmt.Println("Подпись неверна. Где-то ошибка")
	}
}
