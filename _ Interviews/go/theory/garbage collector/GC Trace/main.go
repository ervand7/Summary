package main

func main() {
	a := make([]int, 0)
	for i := 0; i < 3_000_000; i++ {
		a = append(a, i)
	}
}
