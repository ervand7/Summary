package main

import "reflect"

type Person struct {
	ID         uint
	Name       string
	Salary     uint
	Department *Department
	Position   *Position
}
type Department struct {
	ID       uint
	Name     string
	Persons  []*Person
	Head     *Department
	Branches []*Department
}
type Position struct {
	ID   uint
	Name string
}

// и индекс для поиска
// соответствия ID указателю на одну из этих структур
var Index map[uint]interface{}

/*
Напишем функцию, которая будет возвращать Name любого объекта по его
ID, используя индекс:
*/

/* плохо */
// используем рефлексию
func reflectionSearch(id uint) (string, bool) {
	obj, ok := Index[id]
	if ok {
		// устанавливаем динамический тип интерфейсной переменной
		// методами пакета reflection
		val := reflect.ValueOf(obj).Elem()
		for i := 0; i < val.NumField(); i++ {
			if val.Type().Field(i).Name == "Name" {
				return val.Field(i).String(), true
			}
		}
	}
	return "", false
}

/* хорошо */
// используем type assertion
func assertionSearch(id uint) (string, bool) {
	obj, ok := Index[id]
	if ok {
		switch val := obj.(type) {
		// используем конструкцию switch type из базового синтаксиса языка
		case *Person:
			return val.Name, true
		case *Department:
			return val.Name, true
		case *Position:
			return val.Name, true
		}
	}
	return "", false
}
