package main

import (
	"fmt"
	"reflect"
	"strconv"
)

type SomeStruct struct {
	Field int
}

func ChangeFieldByName(v interface{}, fname string, newval int) {
	val := reflect.ValueOf(v)
	if val.Kind() == reflect.Ptr {
		val = val.Elem()
	}
	if val.Kind() != reflect.Struct {
		return
	}

	field := val.FieldByName(fname)
	if field.IsValid() {
		if field.CanSet() {
			switch field.Kind() {
			case reflect.Int:
				field.SetInt(int64(newval))
			case reflect.String:
				field.SetString(strconv.Itoa(newval))
			}
		}
	}
}

func main() {
	someStruct := SomeStruct{Field: 1}
	ChangeFieldByName(someStruct, "Field", 12)
	fmt.Printf("%#v", someStruct) // main.SomeStruct{Field:1}
}
