package main // define current package

import (
	"fmt"
	"reflect"
)

func main() { // func main must be present
	message := "message" // only double quotes
	fmt.Println(message)

	someString := ""
	someString = "filled value"
	fmt.Println(someString)

	var world string = "world"
	var word string
	word = "word"
	fmt.Println(word, world)

	const hello string = ""
	fmt.Println(hello)
	const notUsedAllowedConst string = "notUsedAllowedConst"

	fmt.Println("Type of variable world is", reflect.TypeOf(word))

}
