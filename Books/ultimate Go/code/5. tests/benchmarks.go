package main

import (
	"fmt"
	"testing"
)

var a []int

// BenchmarkSprint Identifying the correct b.N to match the flag -benchtime is
// accomplished through some trial and error. At the very beginning of running
// the benchmark, the tooling will set the value of b.N to 1 and run the loop.
// Then it will multiply the value of b.N by 100 until it gets close to
// the -benchtime.
func BenchmarkSprint(b *testing.B) {
	a = append(a, b.N)
	for i := 0; i < b.N; i++ {
		_ = fmt.Sprint("hello")
	}
	if len(a) > 4 {
		fmt.Println(a)
	}
}

/*
goos: darwin
goarch: arm64
BenchmarkSprint
[1 100 10000 1000000 31889589] <<- LOOK HERE
BenchmarkSprint-8   	31889589	        34.18 ns/op
PASS
*/
