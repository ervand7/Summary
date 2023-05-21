package main

import (
	"bytes"
	"compress/flate"
	"fmt"
	"log"
	"strings"
)

/*
Функции пакетов compress принимают в качестве параметров переменные,
которые реализуют интерфейсы io.Reader и io.Writer. Для компрессии нужно создать
переменную типа Writer, куда будет направлен входящий поток и будут записываться
сжатые данные. За распаковку отвечает переменная типа Reader, в которую отправляются
сжатые данные и из которой читаются уже распакованные.
*/

// Compress сжимает слайс байт.
func Compress(data []byte) ([]byte, error) {
	var b bytes.Buffer
	// создаём переменную w — в неё будут записываться входящие данные,
	// которые будут сжиматься и сохраняться в bytes.Buffer
	w, err := flate.NewWriter(&b, flate.BestCompression)
	if err != nil {
		return nil, fmt.Errorf("failed init compress writer: %v", err)
	}
	// запись данных
	_, err = w.Write(data)
	if err != nil {
		return nil, fmt.Errorf("failed write data to compress temporary buffer: %v", err)
	}
	// обязательно нужно вызвать метод Close() — в противном случае часть данных
	// может не записаться в буфер b; если нужно выгрузить все упакованные данные
	// в какой-то момент сжатия, используйте метод Flush()
	err = w.Close()
	if err != nil {
		return nil, fmt.Errorf("failed compress data: %v", err)
	}
	// переменная b содержит сжатые данные
	return b.Bytes(), nil
}

// Decompress распаковывает слайс байт.
func Decompress(data []byte) ([]byte, error) {
	// переменная r будет читать входящие данные и распаковывать их
	r := flate.NewReader(bytes.NewReader(data))
	defer r.Close()

	var b bytes.Buffer
	// в переменную b записываются распакованные данные
	_, err := b.ReadFrom(r)
	if err != nil {
		return nil, fmt.Errorf("failed decompress data: %v", err)
	}

	return b.Bytes(), nil
}

func main() {
	data := []byte(strings.Repeat(`This is a test message`, 20))
	// сжимаем содержимое data
	b, err := Compress(data)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%d bytes has been compressed to %d bytes\r\n", len(data), len(b))

	// распаковываем сжатые данные
	out, err := Decompress(b)
	if err != nil {
		log.Fatal(err)
	}
	// сравниваем начальные и полученные данные
	if !bytes.Equal(data, out) {
		log.Fatal(`original data != decompressed data`)
	}
}

// 440 bytes has been compressed to 33 bytes
