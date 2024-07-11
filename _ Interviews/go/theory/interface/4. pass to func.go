package main

import "fmt"

// интерфейсное значение передается в функцию как value или pointer в зависимости
// от того, как оно реализовывает интерфейс. Если через value receiver, то
// оно передастся как value, если как pointer receiver, то как pointer.

type SayHelloer interface {
	SayHello() (string, error)
}

// Impl1 implements SayHelloer as value
type Impl1 struct {
	Name string
}

func (s Impl1) SayHello() (string, error) {
	return "Hello", nil
}

// Impl2 implements SayHelloer as pointer
type Impl2 struct {
	Name string
}

func (s *Impl2) SayHello() (string, error) {
	return "Hello", nil
}

func some(n SayHelloer) {
	// здесь ставим точку дебага и смотрим, является ли n указателем или нет
	result, err := n.SayHello()
	if err != nil {
		fmt.Println(err.Error())
	} else {
		fmt.Println(result)
	}
}

func main() {
	var a = Impl1{Name: "Ivan"}
	some(a)

	var b = Impl2{Name: "Vasya"}
	some(&b)
}
