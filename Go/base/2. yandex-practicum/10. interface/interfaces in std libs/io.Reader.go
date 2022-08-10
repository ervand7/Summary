package main

import (
	"errors"
	"fmt"
	"io"
	"strings"
)

func main() {
	s := `Hodor. Hodor hodor, hodor. Hodor hodor hodor hodor hodor. Hodor. Hodor!
		Hodor hodor, hodor; hodor hodor hodor. Hodor. Hodor hodor; hodor hodor - hodor, 
		hodor, hodor hodor. Hodor, hodor. Hodor. Hodor, hodor hodor hodor; hodor hodor; 
		hodor hodor hodor! Hodor hodor HODOR! Hodor hodor... Hodor hodor hodor...`

	// обернём строчку в strings.Reader
	r := strings.NewReader(s)

	// создадим буфер на 16 байт
	b := make([]byte, 16)

	for {
		n, err := r.Read(b)
		if n > 0 {
			// выведем на экран содержимое буфера
			fmt.Printf("%v\n", b)
		}

		if err != nil {
			// если дочитали до конца, выходим из цикла
			if errors.Is(err, io.EOF) {
				break
			}

			// обрабатываем ошибку чтения
			fmt.Printf("error: %v\n", err)
		}
	}
}
