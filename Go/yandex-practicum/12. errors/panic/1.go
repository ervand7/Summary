package main

import "fmt"

func mypanic() {
	defer func() {
		if p := recover(); p != nil {
			fmt.Println(`Возникла паника: `, p)
		}
	}()
	panic(`аварийная ситуация`)
}

func main() {
	fmt.Println("Старт")
	mypanic()
	// функция main продолжит работу, так как использовали recover
	fmt.Println("Финиш")
}

/*
Старт
Возникла паника: аварийная ситуация
Финиш
*/
