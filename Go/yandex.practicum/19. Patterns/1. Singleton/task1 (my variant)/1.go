package main

import (
	"fmt"
	"os"
	"sync"
	"time"
)

var (
	dumpFile *os.File
	once     sync.Once
)

func dump(data []byte) error {
	fmt.Println("Called dump!")
	if dumpFile == nil {
		// создаём файл при первом обращении
		fname, err := os.Executable()
		if err == nil {
			dumpFile, err = os.Create(fname + `.dump`)
		}
		if err != nil {
			panic(err)
		}
	}
	_, err := dumpFile.Write(data)
	return err
}

func Dump(data []byte) {
	once.Do(func() {
		dump(data)
	})
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
