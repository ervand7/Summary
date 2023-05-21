package main

import (
	"fmt"
	"reflect"
	"runtime"
	"time"
)

func countCall(f func(string)) func(string) {
	count := 0
	funcName := runtime.FuncForPC(reflect.ValueOf(f).Pointer()).Name()
	return func(x string) {
		count++
		fmt.Printf("Функция %s вызвана %d раз\n", funcName, count)
		f(x)
	}
}

// metricTimeCall для того, чтобы обернуть уже обернутую функцию
// (countCall оборачивает myPrint)
func metricTimeCall(f func(string)) func(string) {
	return func(s string) {
		start := time.Now()
		f(s)
		fmt.Println("Execution time: ", time.Now().Sub(start))
	}
}

func myPrint(s string) {
	fmt.Println(s)
}

func main() {
	countedPrint := countCall(myPrint)
	countedPrint("Hello world")
	countedPrint("Hi")

	countAndMetricPrint := metricTimeCall(countedPrint)
	countAndMetricPrint("Hello")
	countAndMetricPrint("World")
}

/*
Функция main.myPrint вызвана 1 раз
Hello world

Функция main.myPrint вызвана 2 раз
Hi

Функция main.myPrint вызвана 3 раз
Hello
Execution time:  3.147µs

Функция main.myPrint вызвана 4 раз
World
Execution time:  3.16µs
*/
