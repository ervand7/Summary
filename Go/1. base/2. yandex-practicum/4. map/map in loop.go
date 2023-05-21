package main

import "fmt"

func main() {
	m := make(map[string]string)
	m["foo"] = "bar"
	m["bazz"] = "yup"
	for k, v := range m {
		fmt.Printf("Ключ %v, имеет значение %v \n", k, v)
	}
}

/*
Ключ foo, имеет значение bar
Ключ bazz, имеет значение yup
*/
