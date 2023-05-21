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

	fmt.Println(ctx)
	fmt.Println(cancel)
	fmt.Println(ctx_)
	fmt.Println(cancel_)
}

/*
context.Background.WithDeadline(2022-08-10 17:02:08.191447 +0300 MSK m=+2.000152251 [1.999804292s])
0x10414b680
context.Background.WithDeadline(2022-08-10 17:02:08.191472 +0300 MSK m=+2.000177543 [1.999816459s])
0x10414b680
*/
