package main

import (
	"fmt"
	"reflect"
	"time"
)

type MyType struct {
	User      string    `json:"user,omitempty" example:"Bob"`
	CreatedAt time.Time `json:"created_at"`
}

const (
	targetField = "User" // имя поля, о котором нужно получить информацию
	targetTag   = "json" // тег, значение которого нужно получить
)

func main() {

	obj := MyType{}

	// получаем Go-описание типа
	objType := reflect.ValueOf(obj).Type()

	// ищем поле по имени
	objField, ok := objType.FieldByName(targetField)
	if !ok {
		panic(fmt.Errorf("field (%s): not found", targetField))
	}

	// получаем метаинформацию о поле
	fieldTag := objField.Tag
	// ищем тег по имени
	tagValue, ok := fieldTag.Lookup(targetTag)
	if !ok {
		panic(fmt.Errorf("tag (%s) for field (%s): not found", targetTag, targetField))
	}

	fmt.Printf("Значение тега (%s) поля (%s): %s\n", targetTag, targetField, tagValue)
	fmt.Printf("Теги поля (%s): %s\n", targetField, fieldTag)
	/*
		Значение тега (json) поля (User): user,omitempty
		Теги поля (User): json:"user,omitempty" example:"Bob"
	*/
}
