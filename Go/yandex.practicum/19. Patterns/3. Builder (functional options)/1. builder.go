package main

import "fmt"

type Object struct {
	Mode int
	Path string
}

// SetMode — пример функции, которая присваивает поле Mode
func (o *Object) SetMode(mode int) *Object {
	o.Mode = mode
	return o
}

// SetPath — пример функции, которая присваивает поле Path
func (o *Object) SetPath(path string) *Object {
	o.Path = path
	return o
}

// NewObject — функция-конструктор объекта
func NewObject() *Object {
	return &Object{}
}

func main() {
	o := NewObject().SetMode(10).SetPath(`root`)
	fmt.Printf("%#v", o) // &main.Object{Mode:10, Path:"root"}
}
