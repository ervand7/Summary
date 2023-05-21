package main

import (
	"errors"
	"fmt"
	"os"
)

/*
Go даёт возможность упаковывать ошибки (error wrapping).
Для этого достаточно в функции Errorf добавить к ошибке спецификатор %w.
Исходную ошибку можно получить функцией errors.Unwrap.
*/

func ReadTextFile(filename string) (string, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return ``, fmt.Errorf(`failed reading file: %w`, err)
	}
	return string(data), nil
}

func main() {
	if data, err := ReadTextFile(`myconfig.yaml`); err != nil {
		if os.IsNotExist(errors.Unwrap(err)) && errors.Is(errors.Unwrap(err), os.ErrNotExist) {
			// создаём файл конфигурации
			fmt.Println("Hello")
			return
		}
		fmt.Println(data)
	}
}
