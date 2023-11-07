package main

// If map is not initialized we can not assign new key

func main() {
	var m map[int]string
	m[1] = "hello" // panic: assignment to entry in nil map
}
