package main

import (
	"fmt"
	"reflect"

	"main/some"
)

/*
Мы можем получить доступ к значениям с неэкспортируемыми типами из других
пакетов. Но лучше так не делать.
*/

func main() {
	result := some.NewErvand(1)
	fmt.Println(reflect.TypeOf(result)) // some.ervand

	v := some.VarOfNonExportType
	fmt.Println(reflect.TypeOf(v)) // some.ervand
}
