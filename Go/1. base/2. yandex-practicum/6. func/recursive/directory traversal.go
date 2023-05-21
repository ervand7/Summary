package main

import (
	"fmt"
	"io/ioutil"
	"path/filepath"
)

func main() {
	PrintAllFiles(".")
}

func PrintAllFiles(path string) {
	// получаем список всех элементов в папке (и файлов, и директорий)
	files, err := ioutil.ReadDir(path)
	if err != nil {
		fmt.Println("unable to get list of files", err)
		return
	}
	//  проходим по списку
	for _, f := range files {
		filename := filepath.Join(path, f.Name())
		fmt.Println(filename)
		// если элемент — директория, то вызываем для него рекурсивно ту же функцию
		if f.IsDir() {
			PrintAllFiles(filename)
		}
	}
}
