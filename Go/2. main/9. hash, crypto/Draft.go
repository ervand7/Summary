package main

import (
	"crypto/aes"
	"crypto/cipher"
	"crypto/rand"
	"crypto/sha256"
	"fmt"
)

func GenerateRandom_(size int) ([]byte, error) {
	b := make([]byte, size)
	_, err := rand.Read(b)
	if err != nil {
		return nil, err
	}

	return b, nil
}

type Encrypter struct {
	aesgcm cipher.AEAD
	nonce  []byte
}

func NewEncrypter() *Encrypter {
	key := sha256.Sum256([]byte("x35k9f")) // ключ шифрования
	aesblock, _ := aes.NewCipher(key[:])
	aesgcm, _ := cipher.NewGCM(aesblock)
	nonce, _ := GenerateRandom_(aesgcm.NonceSize())
	return &Encrypter{
		aesgcm: aesgcm,
		nonce:  nonce,
	}
}

func (e *Encrypter) Encrypt(src string) []byte {
	encrypted := e.aesgcm.Seal(nil, e.nonce, []byte(src), nil)
	return encrypted
}

func (e *Encrypter) Decrypt(src []byte) (string, error) {
	decrypted, err := e.aesgcm.Open(nil, e.nonce, src, nil)
	if err != nil {
		fmt.Println(err.Error())
		return "", err
	}
	return string(decrypted), nil
}

func main() {
	n := NewEncrypter()
	encrypted := n.Encrypt("Привет!")
	fmt.Println(encrypted)

	decrypted, _ := n.Decrypt(encrypted)
	fmt.Println(decrypted)
}
