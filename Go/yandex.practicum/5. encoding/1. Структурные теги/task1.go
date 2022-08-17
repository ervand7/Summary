package main

import (
	"fmt"
	"reflect"
	"strconv"
	"strings"
)

// User используется для тестирования.
type User struct {
	Nick string
	Age  int `limit:"18"`
	Rate int `limit:"0,100"`
}

// Str2Int конвертирует строку в int.
func Str2Int(s string) int {
	v, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return v
}

// Validate проверяет min и max для int c тегом limit.
func Validate(obj interface{}) bool {
	vobj := reflect.ValueOf(obj)
	objType := vobj.Type() // получаем описание типа

	// перебираем все поля структуры
	for i := 0; i < objType.NumField(); i++ {
		// берём значение текущего поля
		if v, ok := vobj.Field(i).Interface().(int); ok {
			limitTag, isLimit := objType.Field(i).Tag.Lookup("limit")
			if !isLimit {
				continue
			}
			limits := strings.Split(limitTag, ",")
			if v < Str2Int(limits[0]) {
				return false
			}
			if len(limits) > 1 && v > Str2Int(limits[1]) {
				return false
			}
		}
	}
	return true
}

func main() {
	fmt.Println(
		Validate(User{"admin", 20, 88}),
		Validate(User{"su", 45, 10}),
		Validate(User{"", 16, 5}),
		Validate(User{"usr", 24, -2}),
		Validate(User{"john", 18, 0}),
		Validate(User{"usr2", 30, 200}),
	)
	// программа должна вывести следующее:
	// true true false false true false
}
