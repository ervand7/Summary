package main

import "fmt"

func main() {
	var a = []int{1, 5, 6, 18, 99} // слайсы отсортированы
	var b = []int{2, 4, 9, 11}
	fmt.Println(mergeSorted(a, b))
}

func mergeSorted(a []int, b []int) []int {
	i, j := 0, 0
	var result = make([]int, 0, len(a)+len(b))
	for i < len(a) && j < len(b) {
		if a[i] < b[j] {
			result = append(result, a[i])
			i++
		} else {
			result = append(result, b[j])
			j++
		}
	}

	if i < len(a) {
		result = append(result, a[i:]...)
	}
	if j < len(b) {
		result = append(result, b[j:]...)
	}

	return result
}
