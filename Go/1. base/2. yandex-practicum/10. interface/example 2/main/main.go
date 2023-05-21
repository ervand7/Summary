package main

import (
	"fmt"
	"randbyte"
	"time"
)

func main() {
	param := time.Now()
	paramUnix := param.UnixNano()
	generator := randbyte.New(paramUnix)
	buf := make([]byte, 16)
	for i := 0; i < 5; i++ {
		n, _ := generator.Read(buf)
		fmt.Printf("Generate bytes: %v size(%d)\n", buf, n)
	}
}

/*
Generate bytes: [28 238 99 63 23 168 105 87 0 0 0 0 0 0 0 0] size(16)
Generate bytes: [99 107 18 114 65 106 238 108 0 0 0 0 0 0 0 0] size(16)
Generate bytes: [138 102 231 94 152 62 94 81 0 0 0 0 0 0 0 0] size(16)
Generate bytes: [204 94 228 178 208 49 130 11 0 0 0 0 0 0 0 0] size(16)
Generate bytes: [221 152 77 158 8 40 37 24 0 0 0 0 0 0 0 0] size(16)
*/
