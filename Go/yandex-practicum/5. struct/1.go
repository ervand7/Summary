package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func main() {
	man := Person{"Alex", 30}
	fmt.Printf("Man %#v", man) // Man main.Person{Name:"Alex", Age:30}

}
