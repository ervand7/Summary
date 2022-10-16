// go build -gcflags="-m" gcflags.go
package main

func one(a, b int) int {
	var res = a + b
	return res
}

func second(a, b int) *int {
	var res = a + b
	return &res
}

func main() {
	one(1, 2)
	second(1, 2)
}

/*
./gcflags.go:4:6: can inline one
./gcflags.go:9:6: can inline second
./gcflags.go:14:6: can inline main
./gcflags.go:15:5: inlining call to one
./gcflags.go:16:8: inlining call to second
./gcflags.go:10:6: moved to heap: res
*/
