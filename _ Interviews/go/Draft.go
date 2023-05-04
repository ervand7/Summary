package main

import (
	"context"
	"fmt"
)

func main() {
	// Функцией WithValue можно создать дочерний контекст с «зашитым» в него значением:
	ctx1 := context.WithValue(context.Background(), "key_1", "value_1")
	ctx2 := context.WithValue(ctx1, "key_2", "value_2")
	fmt.Println(ctx2.Value("key_1")) // value_1
}
