package main

import (
	"fmt"
	"io/ioutil"
	"path/filepath"
	"strings"
)

/*
Вот ещё интересный пример применения замыкания.
Вспомним функцию PrintAllFilesWithFilter, с которой мы недавно работали.
Её недостаток в том, что параметр filter передаётся при каждом рекурсивном вызове.
От этого можно избавиться, используя анонимную функцию в качестве замыкания.
*/

func PrintAllFilesWithFilterClosure(path string, filter string) {
	var walk func(string)

	walk = func(p string) {
		files, err := ioutil.ReadDir(p)
		if err != nil {
			fmt.Println("unable to get list of files", err)
			return
		}
		for _, f := range files {
			filename := filepath.Join(p, f.Name())
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
	PrintAllFilesWithFilterClosure(".", "1. base")
}
