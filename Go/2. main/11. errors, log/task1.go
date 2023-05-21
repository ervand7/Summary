package main

import (
	"errors"
	"fmt"
	"log"
	"os"
	"strings"
)

// LabelError описывает ошибку с дополнительной меткой.
type LabelError struct {
	Label string // метка должна быть в верхнем регистре
	Err   error
}

// добавьте методы Error() и NewLabelError(string, error)

func (le *LabelError) Error() string {
	return fmt.Sprintf("[%s] %v", strings.ToUpper(le.Label), le.Err)
}

func NewLabelError(filename string, err error) error {
	return &LabelError{
		Label: filename,
		Err:   fmt.Errorf(`%w`, err),
	}
}

// Unwrap возвращает исходную ошибку.
func (le *LabelError) Unwrap() error {
	return le.Err
}

func main() {
	_, err := os.ReadFile("mytest.txt")
	if err != nil {
		err = NewLabelError("file", err)
	}
	fmt.Println(err) // [FILE] open mytest.txt: no such file or directory

	var le *LabelError
	if errors.As(err, &le) {
		log.Printf(`возникла ошибка: >>> %v <<< с файлом %s`, err, le.Label)
	}

	fmt.Println(errors.Is(err, os.ErrNotExist)) // true
}
