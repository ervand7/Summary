package main

import (
	"crypto/rand"
	"encoding/hex"
	"fmt"
)

/*
В Go сгенерировать криптостойкие случайные байты можно функцией rand.Read
из пакета crypto/rand. В параметре нужно передать слайс байт ненулевой длины,
который будет заполнен случайными байтами. Размер слайса не изменяется.

Чтобы затем использовать полученный массив байт, например для кук,
нужно дополнительно его закодировать. Это можно сделать
функцией hex.EncodeToString из пакета encoding/hex.
*/

func main() {
	// определяем слайс нужной длины
	b := make([]byte, 16)
	_, err := rand.Read(b) // записываем байты в массив b
	if err != nil {
		fmt.Printf("error: %v\n", err)
		return
	}

	fmt.Println(hex.EncodeToString(b)) // b8f22b438300646a0964cf5a3d0eff7a
}