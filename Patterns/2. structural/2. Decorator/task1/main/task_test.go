package main

import (
	"strings"
	"testing"
)

/*
Есть тип, содержащий строку, и структуры-модификаторы Upper и Replace.
Вставьте недостающую реализацию методов Modify и инициализацию переменных
replace и upper в функции TestModifier.
*/

type Modifier interface {
	Modify() string
}

type Original struct {
	Value string
}

func (o *Original) Modify() string {
	return o.Value
}

// Upper возвращает строку в верхнем регистре.
type Upper struct {
	modifier Modifier
}

func (u *Upper) Modify() string {
	return strings.ToUpper(u.modifier.Modify())
}

// Replace заменяет строки old на new.
type Replace struct {
	modifier Modifier
	old      string
	new      string
}

func (r *Replace) Modify() string {
	return r.new
}

func TestModifier(t *testing.T) {
	original := &Original{Value: "Привет, гофер!"}
	replace := &Replace{
		// инициализируйте поля нужными значениями
		modifier: original,
		old:      original.Value,
		new:      "привет, мир!",
	}
	upper := &Upper{
		// инициализируйте поле нужным значением
		modifier: replace,
	}
	if upper.Modify() != "ПРИВЕТ, МИР!" {
		t.Errorf(`get %s`, upper.Modify())
	}
}
