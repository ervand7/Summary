package main

import "time"

func hangingGoRoutine() {
	go time.Sleep(time.Hour * 24)
}
