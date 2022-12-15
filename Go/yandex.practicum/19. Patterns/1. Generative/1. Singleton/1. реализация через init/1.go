package main

import (
	"fmt"
	"time"
)

type singleInstance struct {
}

var singleton *singleInstance

func init() {
	singleton = &singleInstance{}
}

func getSingleton() *singleInstance {
	return singleton
}

func main() {
	for i := 0; i < 10; i++ {
		go func(i int) {
			fmt.Printf("Адрес singleton: %p\n", getSingleton())
		}(i)
	}
	time.Sleep(500 * time.Millisecond)
}
