package main

import "fmt"

func main() {
	incrementCopy := func(i int) {
		i++
	}

	increment := func(i *int) {
		*i++
	}

	i := 42

	incrementCopy(i)
	fmt.Println(i) // 42

	increment(&i)
	fmt.Println(i) // 43

}
