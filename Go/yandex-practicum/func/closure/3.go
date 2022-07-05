package main

import (
	"fmt"
	"io/ioutil"
	"path/filepath"
	"strings"
)

func PrintAllFilesWithFilterСlosure(path string, filter string) {
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
			// получаем имя элемента
			// filepath.Join — функция, которая собирает путь к элементу с разделителями
			filename := filepath.Join(path, f.Name())
			// печатаем имя элемента, если путь к нему содержит filter, который получим из внешнего контекста
			if strings.Contains(filename, filter) {
				fmt.Println(filename)
			}
			// если элемент — директория, то вызываем для него рекурсивно ту же функцию
			if f.IsDir() {
				walk(filename)
			}
		}
	}
	// теперь вызовем функцию walk
	walk(path)
}
func main() {
	PrintAllFilesWithFilterСlosure(".", "lesson")
	PrintAllFilesWithFilterСlosure(".", "Functions")
}
