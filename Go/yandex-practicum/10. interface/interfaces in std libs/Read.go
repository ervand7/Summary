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
		/*
			strings.Reader скопирует 16 байт в b.
			В структуре запоминается последний указатель,
			то есть следующий вызов скопирует следующую порцию из 16 байт.
			Также метод возвращает количество прочитанных байт n и ошибку err
			когда дойдём до конца строки, метод отдаст ошибку io.EOF.
		*/
		n, err := r.Read(b)

		/*
			При работе с интерфейсом io.Reader нужно в первую очередь проверять
			n > 0, затем err != nil.
			Могут быть ситуации, когда часть данных получилось прочитать
			и сохранить в буфер, а затем произошла ошибка.
			В таком случае будут одновременно n > 0 и err != nil
		*/
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
