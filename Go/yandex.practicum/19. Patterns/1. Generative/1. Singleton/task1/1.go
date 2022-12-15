package main

import (
	"fmt"
	"os"
	"sync"
	"time"
)

var (
	dumpFile *os.File
	dumpOnce sync.Once
)

func Dump(data []byte) error {
	dumpOnce.Do(func() {
		fmt.Println("Called dump!")
		fname, err := os.Executable()
		if err == nil {
			dumpFile, err = os.Create(fname + `.dump`)
		}
		if err != nil {
			panic(err)
		}
	})
	_, err := dumpFile.Write(data)
	return err
}

func main() {
	data := make([]byte, 0)
	for i := 0; i < 10; i++ {
		go Dump(data)
	}

	time.Sleep(500 * time.Millisecond)
}

/*
Called dump!
*/
