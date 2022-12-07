package main

import (
	"fmt"
	"reflect"
)

/*
Пример, какие значения компилятор присваивает объявленным переменным:
var i = 10	            int
var f = 5.0	            float64
var s = "Hello, world!"	string
var r = 'Щ'	            rune
var b = true	        bool
*/

func main() {
	var i int  // i будет присвоено значение по умолчанию — 0
	println(i) // 0

	var s string // s будет равна пустой строке
	println(s)   //

	var some, company, country string // определяем три строковых переменных
	println(some, company, country)   //

	var id uint32 = 77
	fmt.Println(id, reflect.TypeOf(id)) // 77 uint32

	var pi float32 = 3.1415
	fmt.Println(pi, reflect.TypeOf(pi)) // 3.1415 float32

	var (
		height, length int
		weight         float64
		name_          string
		company_       = "Рога и копыта"
	)
	println(height, length, weight, name_, company_) // 0 0 +0.000000e+000  Рога и копыта

	// короткая нотация
	i_ := 10
	println(i_) // 10
	f := 5.1
	doublef := 2 * f
	fmt.Println(doublef) // doublef имеет тип float64 и равно 10.2

	int64Var := int64(5)
	fmt.Println(int64Var, reflect.TypeOf(int64Var)) // 5 int64
	float32Var := float32(101.3)
	fmt.Println(float32Var, reflect.TypeOf(float32Var)) // 101.3 float32
	// or
	var int64Var_ int64 = 5
	fmt.Println(int64Var_)
	var floatVar_ float32 = 101.3
	fmt.Println(floatVar_)

	pi_, e_ := 3.1415, 2.7183
	// при уточнении значений нельзя использовать :=, так как
	// обе переменных уже определены
	pi_, e_ = 3.14159, 2.71828
	fmt.Println(pi_, e_) // 3.14159 2.71828
}
