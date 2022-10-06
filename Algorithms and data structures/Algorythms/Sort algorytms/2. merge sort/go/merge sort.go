package main

import (
	"fmt"
)

func merge(a []int, ch chan int) {
	if len(a) == 0 {
		close(ch)
		return
	}

	if len(a) == 1 {
		ch <- a[0]
		close(ch)
		return
	}

	mid := len(a) / 2
	// рекурсия
	ch1 := make(chan int)
	go merge(a[:mid], ch1)

	ch2 := make(chan int)
	go merge(a[mid:], ch2)

	v1, ok1 := <-ch1
	v2, ok2 := <-ch2
	// слияние
	for ok1 || ok2 {
		if (ok1 && ok2 && v1 < v2) || (ok1 && !ok2) {
			ch <- v1
			v1, ok1 = <-ch1
		} else if (ok1 && ok2 && v1 >= v2) || (!ok1 && ok2) {
			ch <- v2
			v2, ok2 = <-ch2
		}
	}

	close(ch)
}

func Merge(unsorted []int) (sorted []int) {
	ch := make(chan int)
	go merge(unsorted, ch)

	for v := range ch {
		sorted = append(sorted, v)
	}
	return
}

func main() {
	arr := []int{53, 134, 73, 13, 33, 8, -1, 0, -25, -154, 15}
	b := Merge(arr)
	fmt.Printf("Sorted: %v", b)
}
