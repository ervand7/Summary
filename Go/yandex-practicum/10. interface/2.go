package main

import (
	"io"
	"log"
	"os"
	"strings"
)

/*
В пакете io есть функция LimitReader(r io.Reader, n int64) io.Reader.
Она ограничивает количество байт, которое можно вычитать из io.Reader.
Запрограммируйте подобную функцию самостоятельно.

Код должен вывести подстроку some.
Подсказка: подумайте, как можно ограничить чтение?
Нужно как-то подсчитывать и запоминать количество байт, оставшихся для чтения из reader.
*/

type LimitedReader struct {
	reader io.Reader
	// запоминаем количество cчитанных байт
	left int
}

func LimitReader(r io.Reader, n int) io.Reader {
	return &LimitedReader{reader: r, left: n}
}

func (r *LimitedReader) Read(p []byte) (int, error) {
	if r.left == 0 {
		return 0, io.EOF
	}
	if r.left < len(p) {
		p = p[0:r.left]
	}
	n, err := r.reader.Read(p)
	r.left -= n
	return n, err
}

func main() {
	r := strings.NewReader("some io.Reader stream to be read\n")
	lr := LimitReader(r, 4)

	_, err := io.Copy(os.Stdout, lr)
	if err != nil {
		log.Fatal(err)
	}
}
