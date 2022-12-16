package main

import "fmt"

/*
Шаблон Итератор позволяет последовательно обходить элементы объектов,
используя единый интерфейс. Но его не следует применять,
если можно обойтись обычным циклом.
Итератор применяется если нужно реализовать единый интерфейс
для обхода элементов различных типов.
Классический вариант реализации Итератора подразумевает существование
соответствующего метода для перебора элементов коллекции. Рассмотрим пример:
*/

// Iterator — интерфейс для получения следующего элемента.
type Iterator interface {
	Next() (string, bool)
}

// Exported — тип, реализующий интерфейс Iterator.
type Exported struct {
	ID        string
	invisible []string
	cursor    int
}

func NewExported(s ...string) *Exported {
	e := new(Exported)
	e.invisible = append(e.invisible, s...)
	return e
}

// Next — реализация Итератора.
func (e *Exported) Next() (string, bool) {
	if e.cursor <= len(e.invisible) {
		e.cursor++
	}
	return e.invisible[e.cursor-1], e.cursor < len(e.invisible)
}

func main() {
	// клиентский код
	e := NewExported("foo", "bar", "buzz", "oups")
	for {
		next, hasNext := e.Next()
		fmt.Println(next)
		if !hasNext {
			break
		}
	}
}

/*
foo
bar
buzz
oups
*/
