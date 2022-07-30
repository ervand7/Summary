package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	// Кроме ручной отмены контекста, в Go есть возможность отменять
	// контекст автоматически по истечении времени:
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)

	// Если нужно отменить контекст в определённый момент времени,
	// поможет функция-сестра WithDeadline:
	d := time.Now().Add(2 * time.Second)
	ctx_, cancel_ := context.WithDeadline(context.Background(), d)

	fmt.Println(ctx, cancel, ctx_, cancel_)
}
