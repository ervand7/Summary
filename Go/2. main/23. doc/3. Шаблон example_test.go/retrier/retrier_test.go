package retrier

import (
	"context"
	"fmt"
	"time"
)

func Example() {
	op := func(_ context.Context) error {
		return fmt.Errorf("что-то пошло не так")
	}

	// Определяем контекст с ограничением по времени.
	opCtx, opCancel := context.WithTimeout(context.Background(), 200*time.Millisecond)
	defer opCancel()

	// Выполняем операцию op, переопределяя стандартные значения min и max.
	Do(opCtx, op, WithMinMaxDelay(50*time.Millisecond, 1*time.Second))
}
