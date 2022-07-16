package main

import "fmt"

func main() {
	i := 42
	p := &i
	fmt.Println(*p) // читаем значение переменной i через указатель p
	*p = 21         // записываем в переменную i значение 21 через указатель p
	fmt.Println(p)  // 0x1400012c008
	fmt.Println(i)  // 21

}
