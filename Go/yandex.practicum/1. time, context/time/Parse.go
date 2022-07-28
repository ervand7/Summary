package main

import (
	"fmt"
	"time"
)

func main() {
	t, _ := time.Parse(time.UnixDate, "Tue Jun 1 22:16:03 MSK 2021")
	fmt.Println(t) // 2021-06-01 22:16:03 +0300 MSK
}
