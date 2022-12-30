package main

import (
	"go/ast"
	"go/parser"
	"go/printer"
	"go/token"
	"os"
)

/*
Замените имя переменной id на Ident в коде, который содержит переменная src.
Выведите изменённое AST функцией printer.Fprint().
*/

func main() {
	src := `
		package main
			
		func main() {
			 ids := 77
			 id := ids + 1
			 fmt.Println("id равно:", id/2 )
		}
	`

	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, "", src, 0)
	if err != nil {
		panic(err)
	}
	ast.Inspect(f, func(n ast.Node) bool {
		if v, ok := n.(*ast.Ident); ok && v.Name == `id` {
			v.Name = `Ident`
		}
		return true
	})
	printer.Fprint(os.Stdout, fset, f)
}
