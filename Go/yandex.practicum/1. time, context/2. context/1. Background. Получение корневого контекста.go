package main

import (
	"context"
	"fmt"
)

func main() {
	// Background всегда отдаёт ссылку на один и тот же глобальный объект.
	fmt.Println(context.Background() == context.Background()) // true

	// Есть похожая функция, которая тоже отдаёт корневой контекст:
	fmt.Println(context.TODO() == context.TODO()) // true
}
