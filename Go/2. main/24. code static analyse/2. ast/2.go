package main

import (
	"fmt"
	"go/ast"
	"go/parser"
	"go/printer"
	"go/token"
	"os"
)

func main() {
	// текст исходного кода
	src := `
        package main
        import "fmt"
        
        func calc(a int) {
           b := (a+8)*2
           return b
        }
        
        func main() {
            fmt.Println(calc(3), calc(5))
            fmt.Println("Hello, world!")
        }
`
	// создаём token.FileSet
	fset := token.NewFileSet()
	// получаем дерево разбора
	f, err := parser.ParseFile(fset, "", src, parser.AllErrors)
	if err != nil {
		fmt.Println(err)
	}
	// запускаем инспектор, который рекурсивно обходит ветви AST
	// передаём инспектирующую функцию анонимно
	ast.Inspect(f, func(n ast.Node) bool {
		// проверяем, какой конкретный тип лежит в узле
		switch x := n.(type) {
		case *ast.CallExpr:
			// ast.CallExpr представляет вызов функции или метода
			fmt.Printf("CallExpr %v: ", fset.Position(x.Fun.Pos()))
			printer.Fprint(os.Stdout, fset, x)
			fmt.Println()
		case *ast.FuncDecl:
			// ast.FuncDecl представляет декларацию функции
			fmt.Printf("FuncDecl %s %v: ", x.Name.Name, fset.Position(x.Pos()))
			printer.Fprint(os.Stdout, fset, x)
			fmt.Println()
		}
		return true
	})
}

/*
FuncDecl calc 5:9: func calc(a int) {
        b := (a + 8) * 2
        return b
}
FuncDecl main 10:9: func main() {
        fmt.Println(calc(3), calc(5))
        fmt.Println("Hello, world!")
}
CallExpr 11:13: fmt.Println(calc(3), calc(5))
CallExpr 11:25: calc(3)
CallExpr 11:34: calc(5)
CallExpr 12:13: fmt.Println("Hello, world!")
*/
