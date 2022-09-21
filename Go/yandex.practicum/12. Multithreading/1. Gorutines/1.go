package main

import (
	"fmt"
	"time"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		fmt.Print(s + ` `)
		time.Sleep(50 * time.Millisecond)
	}
}

func main() {
	// создадим горутину с функцией say
	go say(`hello`)
	// создадим горутину с анонимной функцией
	go func() {
		say(`world`)
	}()
	// обычный вызов функции say
	say(`bye`)
}

// bye world hello hello world bye world bye hello world hello bye world bye hello
