package main

import "fmt"

func main() {
	weekTempArr := [7]int{1, 2, 3, 4, 5, 6, 7}

	workDaysSlice := weekTempArr[:5]
	fmt.Println(workDaysSlice, len(workDaysSlice), cap(workDaysSlice)) // [1 2 3 4 5] 5 7

	weekendSlice := weekTempArr[5:]
	fmt.Println(weekendSlice, len(weekendSlice), cap(weekendSlice)) // [6 7] 2 2

	fromTuesdayToThursDaySlice := weekTempArr[1:4]
	fmt.Println(
		fromTuesdayToThursDaySlice,
		len(fromTuesdayToThursDaySlice),
		cap(fromTuesdayToThursDaySlice)) // [2 3 4] 3 6

	weekTempSlice := weekTempArr[:]
	fmt.Println(weekTempSlice, len(weekTempSlice), cap(weekTempSlice)) // [1 2 3 4 5 6 7] 7 7
}
