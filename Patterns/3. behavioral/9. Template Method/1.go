package main

import (
	"fmt"
	"sort"
)

/*
Паттерн Шаблонный метод используется, когда:
 - есть основная часть алгоритма, но детали могут различаться для объектов разных типов;
 - нужно расширить алгоритм, не изменяя основных шагов.
Применение этого паттерна в Go можно показать на примере пакета sort
стандартной библиотеки. Чтобы для элементов объекта-последовательности
использовать сортировку пакета sort, достаточно для типа этого объекта
реализовать интерфейс sort.Interface:
*/

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("%s: %d", p.Name, p.Age)
}

type ByAge []Person

// реализуем интерфейс sort.Interface для сортировки по возрасту

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

// Sort сортирует слайс ByAge, так он реализует интерфейс sort.Interface.
func (a ByAge) Sort() {
	sort.Sort(a)
}

func main() {
	people := ByAge{
		{"Bob", 31},
		{"John", 48}, // John старший
		{"Michael", 17},
		{"John", 26}, // John младший
	}

	fmt.Println(people) // [Bob: 31 John: 48 Michael: 17 John: 26]
	// можем применить шаблонный метод
	people.Sort()
	fmt.Println(people) // [Michael: 17 John: 26 Bob: 31 John: 48]
}
