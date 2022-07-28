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
	var walk func(string)
	walk = func(path string) {
		files, err := ioutil.ReadDir(path)
		if err != nil {
			fmt.Println("unable to get list of files", err)
			return
		}
		for _, f := range files {
			filename := filepath.Join(path, f.Name())
			if f.IsDir() {
				if predicate(filename) != true {
					fmt.Printf("\nDirectory %s does not contain dot in it name", filename)
				}
				walk(filename)
			}
		}
	}
	walk(path)
}
func main() {
	PrintFilesWithFuncFilter(".", containsDot)
}
