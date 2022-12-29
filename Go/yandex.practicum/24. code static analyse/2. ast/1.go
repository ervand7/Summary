package main

import (
	"go/ast"
	"go/parser"
	"go/token"
)

func main() {
	// исходный код, который будем разбирать
	src := `
	package main
	import "fmt"
	
	func main() {
		fmt.Println("Hello, world!")
	}
`

	// дерево разбора AST ассоциируется с набором исходных файлов FileSet
	fset := token.NewFileSet()
	// парсер может работать с файлом
	// или исходным кодом, переданным в виде строки
	f, err := parser.ParseFile(fset, "", src, 0)
	if err != nil {
		panic(err)
	}
	// печатаем дерево
	ast.Print(fset, f)
}

/*
    0  *ast.File {
    1  .  Package: 2:2
    2  .  Name: *ast.Ident {
    3  .  .  NamePos: 2:10
    4  .  .  Name: "main"
    5  .  }
    6  .  Decls: []ast.Decl (len = 2) {
    7  .  .  0: *ast.GenDecl {
    8  .  .  .  TokPos: 3:2
    9  .  .  .  Tok: import
   10  .  .  .  Lparen: -
   11  .  .  .  Specs: []ast.Spec (len = 1) {
   12  .  .  .  .  0: *ast.ImportSpec {
   13  .  .  .  .  .  Path: *ast.BasicLit {
   14  .  .  .  .  .  .  ValuePos: 3:9
   15  .  .  .  .  .  .  Kind: STRING
   16  .  .  .  .  .  .  Value: "\"fmt\""
   17  .  .  .  .  .  }
   18  .  .  .  .  .  EndPos: -
   19  .  .  .  .  }
   20  .  .  .  }
   21  .  .  .  Rparen: -
   22  .  .  }
   23  .  .  1: *ast.FuncDecl {
   24  .  .  .  Name: *ast.Ident {
   25  .  .  .  .  NamePos: 5:7
   26  .  .  .  .  Name: "main"
   27  .  .  .  .  Obj: *ast.Object {
   28  .  .  .  .  .  Kind: func
   29  .  .  .  .  .  Name: "main"
   30  .  .  .  .  .  Decl: *(obj @ 23)
   31  .  .  .  .  }
   32  .  .  .  }
   33  .  .  .  Type: *ast.FuncType {
   34  .  .  .  .  Func: 5:2
   35  .  .  .  .  Params: *ast.FieldList {
   36  .  .  .  .  .  Opening: 5:11
   37  .  .  .  .  .  Closing: 5:12
   38  .  .  .  .  }
   39  .  .  .  }
   40  .  .  .  Body: *ast.BlockStmt {
   41  .  .  .  .  Lbrace: 5:14
   42  .  .  .  .  List: []ast.Stmt (len = 1) {
   43  .  .  .  .  .  0: *ast.ExprStmt {
   44  .  .  .  .  .  .  X: *ast.CallExpr {
   45  .  .  .  .  .  .  .  Fun: *ast.SelectorExpr {
   46  .  .  .  .  .  .  .  .  X: *ast.Ident {
   47  .  .  .  .  .  .  .  .  .  NamePos: 6:3
   48  .  .  .  .  .  .  .  .  .  Name: "fmt"
   49  .  .  .  .  .  .  .  .  }
   50  .  .  .  .  .  .  .  .  Sel: *ast.Ident {
   51  .  .  .  .  .  .  .  .  .  NamePos: 6:7
   52  .  .  .  .  .  .  .  .  .  Name: "Println"
   53  .  .  .  .  .  .  .  .  }
   54  .  .  .  .  .  .  .  }
   55  .  .  .  .  .  .  .  Lparen: 6:14
   56  .  .  .  .  .  .  .  Args: []ast.Expr (len = 1) {
   57  .  .  .  .  .  .  .  .  0: *ast.BasicLit {
   58  .  .  .  .  .  .  .  .  .  ValuePos: 6:15
   59  .  .  .  .  .  .  .  .  .  Kind: STRING
   60  .  .  .  .  .  .  .  .  .  Value: "\"Hello, world!\""
   61  .  .  .  .  .  .  .  .  }
   62  .  .  .  .  .  .  .  }
   63  .  .  .  .  .  .  .  Ellipsis: -
   64  .  .  .  .  .  .  .  Rparen: 6:30
   65  .  .  .  .  .  .  }
   66  .  .  .  .  .  }
   67  .  .  .  .  }
   68  .  .  .  .  Rbrace: 7:2
   69  .  .  .  }
   70  .  .  }
   71  .  }
   72  .  Scope: *ast.Scope {
   73  .  .  Objects: map[string]*ast.Object (len = 1) {
   74  .  .  .  "main": *(obj @ 27)
   75  .  .  }
   76  .  }
   77  .  Imports: []*ast.ImportSpec (len = 1) {
   78  .  .  0: *(obj @ 12)
   79  .  }
   80  .  Unresolved: []*ast.Ident (len = 1) {
   81  .  .  0: *(obj @ 46)
   82  .  }
   83  }
*/
