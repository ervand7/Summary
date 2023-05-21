package main

import "fmt"

/*
Создайте слайс и заполните его числами от 1 до 100. Оставьте в
слайсе первые и последние 10 элементов и разверните слайс в обратном порядке.
Подумайте, можно ли подобным образом развернуть строку?
*/
func main() {
	var mySlice []int
	for i := 1; i <= 100; i++ {
		mySlice = append(mySlice, i)
	}
	fmt.Println(mySlice) // [1, 2, 3 ... 100]

	mySlice = append(mySlice[:10], mySlice[90:]...)
	fmt.Println(mySlice) // [1 2 3 4 5 6 7 8 9 10 91 92 93 94 95 96 97 98 99 100]

	for i, j := 0, len(mySlice)-1; i < j; i, j = i+1, j-1 {
		mySlice[i], mySlice[j] = mySlice[j], mySlice[i]
	}
	fmt.Println(mySlice) // [100 99 98 97 96 95 94 93 92 91 10 9 8 7 6 5 4 3 2 1]
}
