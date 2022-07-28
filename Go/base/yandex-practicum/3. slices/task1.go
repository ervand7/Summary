package main

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
	println(mySlice) // [100/128]0x1400006c000

	mySlice = append(mySlice[:10], mySlice[90:]...)
	println(mySlice) // [20/128]0x1400009c000

	for i, j := 0, len(mySlice)-1; i < j; i, j = i+1, j-1 {
		mySlice[i], mySlice[j] = mySlice[j], mySlice[i]
	}
	println(mySlice) // [20/128]0x1400009c000
}
