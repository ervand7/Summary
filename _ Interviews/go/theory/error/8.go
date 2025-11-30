package main

import (
	"errors"
	"fmt"
)

// Deferred function should never return anything.

// Если вы хотите, чтобы defer изменил возвращаемое значение функции,
// у функции должен быть именованный возвращаемый параметр,
// и defer должен присвоить именно его.

func safeExecute() error {
	defer func() error {
		if r := recover(); r != nil {
			// BUG: возвращаем ошибку, но она НИКОГДА НЕ УСТАНАВЛИВАЕТСЯ как return у safeExecute
			return errors.New(fmt.Sprint(r))
		}
		return nil
	}()

	panic("boom")

	return nil
}

func main() {
	err := safeExecute()

	if err != nil {
		fmt.Println("ERROR:", err)
	} else {
		fmt.Println("NO ERROR")
	}
}
