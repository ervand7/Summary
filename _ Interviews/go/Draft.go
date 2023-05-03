package main

import (
	"fmt"
	"sync"
)

const maxCap = 1024

var bytesPool = sync.Pool{
	//
	New: func() interface{} { return []byte{} },
}

// положить
func putBytes(b []byte) {
	if cap(b) <= maxCap {
		b = b[:0] // сброс
		bytesPool.Put(b)
	}
}

// получить
func getBytes() (b []byte) {
	ifc := bytesPool.Get()
	if ifc != nil {
		b = ifc.([]byte)
	}
	return b
}

func main() {
	slice := make([]byte, 10, 10)
	putBytes(slice)
	result := getBytes()
	fmt.Println(result)
}
