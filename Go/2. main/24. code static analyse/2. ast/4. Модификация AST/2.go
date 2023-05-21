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
Теперь сделаем то же самое, но с более тонкой настройкой. При обходе дерева
функцией ast.Inspect() найдём не просто лексически совпадающий литерал,
а именно строку, передаваемую аргументом при вызове функции Println(), и
переведём в верхний регистр.
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
	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, "", src, 0)
	if err != nil {
		panic(err)
	}
	// обходим дерево разбора
	ast.Inspect(f, func(n ast.Node) bool {
		// интересуют только вызовы функций
		if c, ok := n.(*ast.CallExpr); ok {
			if s, ok := c.Fun.(*ast.SelectorExpr); ok {
				// только функции Println
				if s.Sel.Name == "Println" {
					if a, ok := c.Args[0].(*ast.BasicLit); ok {
						// изменяем узел
						a.Value = strings.ToUpper(a.Value)
					}
				}
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
        fmt.Println("HELLO, WORLD!")
}
*/
