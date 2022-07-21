package main

import (
	"fmt"
	"reflect"
)

type MyType_ struct{}

func NaiveIsNil(obj interface{}) bool {
	return obj == nil
}

func IsNil(obj interface{}) bool {
	if obj == nil {
		return true
	}

	objValue := reflect.ValueOf(obj)
	// проверяем, что тип значения ссылочный, то есть в принципе может быть равен nil
	if objValue.Kind() != reflect.Ptr {
		return false
	}
	// проверяем, что значение равно nil
	//  важно, что IsNil() вызывает панику, если value не является ссылочным типом. Поэтому всегда проверяйте на Kind()
	if objValue.IsNil() {
		return true
	}

	return false
}

func main() {
	var t *MyType_
	fmt.Printf("Проверка типа (%v) на nil: %v\n", reflect.TypeOf(t), NaiveIsNil(t))
	fmt.Printf("Проверка типа (%v) на nil: %v\n", reflect.TypeOf(t), IsNil(t))
}

// Проверка типа (*main.MyType_) на nil: false
// Проверка типа (*main.MyType_) на nil: true
