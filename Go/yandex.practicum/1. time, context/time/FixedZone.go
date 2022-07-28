package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	// 2021-07-14 22:30:27.478879 +0300 MSK

	// В этом примере задан часовой пояс, смещённый на 30 минут относительно UTC
	loc := time.FixedZone("My best zone", 30*60)
	fmt.Println(now.In(loc))
	// 2021-07-14 20:00:27.478879 +0030 My best zone
}
