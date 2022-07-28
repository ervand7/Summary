package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	timeStr := now.Format("1.2.06 3:4:5 -07 MST")
	fmt.Println(timeStr) // 7.27.22 8:39:57 +03 MSK
}
