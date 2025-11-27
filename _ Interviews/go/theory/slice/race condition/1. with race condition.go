package main

import "fmt"

func main() {
	s := make([]int, 0, 10000)

	for i := 0; i < 10000; i++ {
		go func(v int) {
			s = append(s, v)
		}(i)
	}

	fmt.Println(len(s)) // 9691
}
