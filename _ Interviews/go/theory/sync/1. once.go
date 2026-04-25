package main

import (
	"fmt"
	"sync"
	"time"
)

var once sync.Once

func initConfig() {
	fmt.Println("Config initialized")
}

func main() {
	for i := 0; i < 5; i++ {
		go func() {
			once.Do(initConfig)
		}()
	}

	time.Sleep(time.Second)
}
