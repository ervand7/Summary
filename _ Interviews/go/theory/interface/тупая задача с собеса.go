package main

import "fmt"

// Because after assigning `data` to the interface, the interface is no longer nil
// since it now contains a type (`*byte`) even though the stored value is nil.

func main() {
	var data *byte
	var in interface{}

	fmt.Println(data, data == nil)
	fmt.Println(in, in == nil)

	in = data
	fmt.Println(in, in == nil)
}
