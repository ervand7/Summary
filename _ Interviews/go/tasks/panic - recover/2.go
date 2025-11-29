package main

import (
	"fmt"
	"time"
)

// the same

func main() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in main:", r)
		}
	}()

	go func() {
		defer func() {
			if r := recover(); r != nil {
				fmt.Println("Recovered in first goroutine:", r)
			}
		}()

		go func() {
			defer func() {
				if r := recover(); r != nil {
					fmt.Println("Recovered in second goroutine:", r)
				}
			}()

			go func() {
				panic("boom-deep")
			}()
		}()
	}()

	time.Sleep(time.Second)
}
