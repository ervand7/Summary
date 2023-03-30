package main

import (
	"bytes"
	"fmt"
)

func main() {
	path := []byte("AAAA/BBBBBBBBB")
	sepIndex := bytes.LastIndexByte(path, '/')
	dir1 := path[:sepIndex]
	dir2 := path[sepIndex+1:]
	dir1 = append(dir1, "suffix"...)
	fmt.Printf("%s\n", dir1) // AAAAsuffix
	fmt.Printf("%s\n", dir2) // uffixBBBB
	fmt.Printf("%s\n", path) // AAAAsuffixBBBB
}
