package main

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

type Iterator[V any] interface {
	First() (V, bool)
	Next() (V, bool)
	Set(V)
}

func Map[I Iterator[V], V any](it I, f func(V) V) {
	for item, ok := it.First(); ok; item, ok = it.Next() {
		it.Set(f(item))
	}
}

// Item — элемент списка со ссылкой на следующий элемент.
type Item[T any] struct {
	next  *Item[T]
	value T
}

// List — список.
type List[T any] struct {
	first *Item[T] // первый элемент
	cur   *Item[T] // текущий элемент
}

func NewList[V any](l *Item[V]) *List[V] {
	var i List[V]
	i.first = l
	i.cur = l
	return &i
}

func (l *List[T]) Next() (T, bool) {
	if l.cur.next != nil {
		l.cur = l.cur.next
		return l.cur.value, true
	}
	var empty T
	return empty, false
}

func (l *List[T]) First() (T, bool) {
	l.cur = l.first
	if l.cur == nil {
		var empty T
		return empty, false
	}
	return l.cur.value, true
}

func (l *List[T]) Set(v T) {
	if l.cur != nil {
		l.cur.value = v
	}
}

func Double[T constraints.Ordered](v T) T {
	return v + v
}

func main() {
	// создаём первый элемент
	li := new(Item[int])
	// добавляем элементы
	for i := 1; i < 7; i++ {
		nl := new(Item[int])
		nl.value = i
		nl.next = li
		li = nl
	}
	// конструируем список
	var list = NewList(li)
	for item, ok := list.First(); ok; item, ok = list.Next() {
		fmt.Println(item)
	}
	Map(list, Double[int])
	fmt.Println("After Mapping")
	for item, ok := list.First(); ok; item, ok = list.Next() {
		fmt.Println(item)
	}
}

/*
6
5
4
3
2
1
0
After Mapping
12
10
8
6
4
2
0
*/
