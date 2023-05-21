package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"fmt"
)

func generateRandom_(size int) ([]byte, error) {
	b := make([]byte, size)
	_, err := rand.Read(b)
	if err != nil {
		return nil, err
	}

	return b, nil
}

func main() {
	src := []byte("Привет!") // данные, которые хотим зашифровать
	fmt.Printf("original: %s\n", src)

	// будем использовать AES256, создав ключ длиной 32 байта
	key := sha256.Sum256([]byte("x35k9f")) // ключ шифрования

	aesblock, err := aes.NewCipher(key[:])
	if err != nil {
		fmt.Printf("error: %v\n", err)
		return
	}

	aesgcm, err := cipher.NewGCM(aesblock)
	if err != nil {
		fmt.Printf("error: %v\n", err)
		return
	}

	// создаём вектор инициализации
	nonce, err := generateRandom_(aesgcm.NonceSize())
	if err != nil {
		fmt.Printf("error: %v\n", err)
		return
	}

	dst := aesgcm.Seal(nil, nonce, src, nil) // зашифровываем
	fmt.Printf("encrypted: %x\n", dst)

	src2, err := aesgcm.Open(nil, nonce, dst, nil) // расшифровываем
	if err != nil {
		fmt.Printf("error: %v\n", err)
		return
	}
	fmt.Printf("decrypted: %s\n", src2)
}
