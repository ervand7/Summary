package main

import (
	"context"
	"fmt"
	"time"
)

func main() {

	ctx := context.Background()
	go func(ctx context.Context) {
		for i := 0; i < 1000; i++ {
			fmt.Println(i)
			if i == 50 {
				<-ctx.Done()
			}
		}
	}(ctx)
	time.Sleep(time.Second)
}
