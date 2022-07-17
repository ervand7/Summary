package main

import (
	"fmt"
	"io/ioutil"
	"path/filepath"
	"strings"
)

// containsDot возвращает все пути, содержащие точки
func containsDot(s string) bool {
	return strings.Contains(s, ".")
}

func PrintFilesWithFuncFilter(path string, predicate func(string) bool) {
	// создаём переменную, содержащую функцию обхода
	// мы создаём её заранее, а не через оператор :=, чтобы замыкание могло сослаться на него
	var walk func(string)
	walk = func(path string) {
		// получаем список всех элементов в папке (и файлов, и директорий)
		files, err := ioutil.ReadDir(path)
		if err != nil {
			fmt.Println("unable to get list of files", err)
			return
		}
		//  проходим по списку
		for _, f := range files {
			/*
				получаем имя элемента
				filepath.Join — функция, которая собирает путь к элементу
				с разделителями
			*/
			filename := filepath.Join(path, f.Name())
			// если элемент — директория, то вызываем для него рекурсивно ту же функцию
			if f.IsDir() {
				if predicate(filename) != true {
					fmt.Printf("\nDirectory %s does not contain dot in it name", filename)
				}
				walk(filename)
			}
		}
	}
	// теперь вызовем функцию walk
	walk(path)
}
func main() {
	PrintFilesWithFuncFilter(".", containsDot)
}
