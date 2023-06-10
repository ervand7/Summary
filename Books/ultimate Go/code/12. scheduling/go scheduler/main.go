package main

import (
	"fmt"
	"runtime"
)

func main() {
	// GOMAXPROCS returns the number of logical
	// CPUs currently being used by the current process.
	fmt.Println(runtime.GOMAXPROCS(0))
}
