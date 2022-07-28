package main

import (
	"fmt"
	"time"
)

/*
На примере этого кода можно увидеть, что пока главная функция занята работой,
функция AfterFunc позволяет параллельно запустить горутину:
*/
func main() {
	time.AfterFunc(1*time.Second, func() {
		fmt.Println("hi from AfterFunc")
	})
	fmt.Println("hi")
	time.Sleep(2 * time.Second)
	fmt.Println("goodbye")
}
