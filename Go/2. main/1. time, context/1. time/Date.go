package main

import (
	"fmt"
	"time"
)

/*
Разобравшись с типами Time и Location, вы можете создать
собственную временную точку — например, время начала 2020 года в UTC:
*/
func main() {
	newYear := time.Date(2020, time.January, 1, 0, 0, 0, 0, time.UTC)
	fmt.Println(newYear) // 2020-01-01 00:00:00 +0000 UTC
}
