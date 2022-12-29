package main

import (
	"go/ast"
	"go/parser"
	"go/printer"
	"go/token"
	"os"
	"strings"
)

/*
Вот простейший и потому немного синтетический пример. Разберём
"Hello, world!", найдём в дереве нужный литерал, поменяем его и зальём
изменённое дерево обратно в исходный код.
*/

func main() {
	// текст исходного кода
	src := `
		package main
		import "fmt"
		
		func main() {
			fmt.Println("Hello, world!")
		}
	`
	// FileSet
	fset := token.NewFileSet()
	// парсинг
	f, err := parser.ParseFile(fset, "", src, 0)
	if err != nil {
		panic(err)
	}
	// обходим дерево разбора
	ast.Inspect(f, func(n ast.Node) bool {
		// если узел имеет тип *ast.BasicLit
		if v, ok := n.(*ast.BasicLit); ok {
			// и содержит подстроку "Hello"
			if strings.Contains(v.Value, "Hello") {
				// изменяем узел
				v.Value = `"Hello, Gopher!"`
			}
		}
		return true
	})
	// выливаем изменённый AST обратно в текст исходного кода и выводим в консоль
	printer.Fprint(os.Stdout, fset, f)
}

/*
package main

import "fmt"

func main() {
        fmt.Println("Hello, Gopher!")
}
*/
