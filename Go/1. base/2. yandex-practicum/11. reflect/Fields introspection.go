package main

import (
	"fmt"
	"reflect"
)

func ExtendedPrint(v interface{}) {
	val := reflect.ValueOf(v)
	//  проверяем, не передали ли нам указатель на структуру
	switch val.Kind() {
	case reflect.Ptr:
		// если нам передали указатель, но он не указатель на структуру
		if val.Elem().Kind() != reflect.Struct {
			fmt.Printf(
				"Pointer to %v : %v",
				val.Elem().Type(),
				val.Elem(),
			)
			return
		}
		// если всё-таки это указатель на структуру — дальше будем работать с самой структурой
		val = val.Elem()

	case reflect.Struct: // работаем со структурой
	default:
		fmt.Printf("%v : %v", val.Type(), val)
		return
	}

	fmt.Printf(
		"Struct of type %v and number of fields %d:\n",
		val.Type(),
		val.NumField(),
	)
	for fieldIndex := 0; fieldIndex < val.NumField(); fieldIndex++ {
		field := val.Field(fieldIndex)
		fmt.Printf(
			"\tField %v: %v - val :%v\n",
			val.Type().Field(fieldIndex).Name,
			field.Type(),
			field,
		)
	}
}

type MyStruct struct {
	A int
	B string
	C bool
}

func main() {
	s := MyStruct{
		A: 3,
		B: "some",
		C: false,
	}
	s1 := &MyStruct{
		A: 7,
		B: "text",
		C: true,
	}

	ExtendedPrint(s)
	ExtendedPrint(s1)
	ExtendedPrint(struct {
		E int
		C string
	}{2, "other text"})
	ExtendedPrint("some string")
}

/*
Struct of type main.MyStruct and number of fields 3:
        Field A: int - val :3
        Field B: string - val :some
        Field C: bool - val :false
Struct of type main.MyStruct and number of fields 3:
        Field A: int - val :7
        Field B: string - val :text
        Field C: bool - val :true
Struct of type struct { E int; C string } and number of fields 2:
        Field E: int - val :2
        Field C: string - val :other text
string : some string
*/
