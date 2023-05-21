package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())

	fmt.Println("Hello, World!")
	time.AfterFunc(1*time.Second, cancel)

	<-ctx.Done()
	fmt.Println("context canceled")
}
