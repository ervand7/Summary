package main

import "fmt"

/*
В языке Go вместо паттерна Строитель чаще всего применяют паттерн Функциональные опции.
Этот шаблон помогает решить те же задачи, но в полной мере использует возможности языка.
Суть паттерна заключается в том, что для параметров создаются функции с замыканием,
которые в свою очередь возвращают функции, принимающие объект и присваивающие ему
нужный параметр.
*/

type object struct {
	Mode int
	Path string
}

// WithMode — пример функции, которая присваивает поле Mode
func WithMode(mode int) func(*object) {
	return func(o *object) {
		o.Mode = mode
	}
}

// WithPath — пример функции, которая присваивает поле Path
func WithPath(path string) func(*object) {
	return func(o *object) {
		o.Path = path
	}
}

// newObject — функция-конструктор объекта
func newObject(opts ...func(*object)) *object {
	o := &object{}

	// вызываем все указанные функции для установки параметров
	for _, opt := range opts {
		opt(o)
	}
	return o
}

func main() {
	o := newObject(WithMode(10), WithPath(`root`))
	fmt.Printf("%#v", o) // &main.object{Mode:10, Path:"root"}
}
