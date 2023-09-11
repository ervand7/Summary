package main

import (
	"fmt"
	"reflect"

	"main/some"
)

/*
Мы можем получить доступ к не экспортируемым сущностям из других пакетов.
Но лучше так не делать.
*/

func main() {
	result := some.NewIvan(1)
	unexported := reflect.TypeOf(result)
	fmt.Println(unexported) // some.ivan

	v := some.VarOfNonExportType
	fmt.Println(reflect.TypeOf(v)) // some.ivan
}
