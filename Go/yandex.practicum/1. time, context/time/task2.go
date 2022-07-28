package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	fmt.Println(now.Format(time.UnixDate)) // Wed Jul 27 20:56:35 MSK 2022
}
