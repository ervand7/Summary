package main

import (
	"time"
)

func main() {
	a := time.NewTimer(0)
	a.Reset(time.Second * 3)
}
