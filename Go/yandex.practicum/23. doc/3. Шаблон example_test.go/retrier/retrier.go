// Модуль retrier повторяет операцию до тех пор, пока она не завершится успешно.
// Задержка между повторами ограничивается сверху и снизу и вычисляется по формуле:
//  delay = delay * multiplier.
package retrier

import (
	"context"
	"errors"
	"fmt"
	"time"
)

// DefaultMultiplier — коэффициент увеличения задержки при повторе.
const DefaultMultiplier = 1.5

// Настройки задержки по умолчанию.
const (
	DefaultMinDelay = 50 * time.Millisecond // минимальный уровень
	DefaultMaxDelay = 1 * time.Second       // максимальный уровень
)

type (
	// Operation определяет операцию повтора.
	Operation func(ctx context.Context) error

	// Option изменяет параметры вычисления задержки для вызова Do.
	Option func(cfg *config)

	// config хранит параметры расчёта задержки между повторами.
	// Этот тип не отобразится в документации.
	config struct {
		// minDelay — минимальное время.
		minDelay time.Duration
		// maxDelay — максимальное время.
		maxDelay time.Duration
		// multiplier — коэффициент изменения задержки.
		multiplier float64
	}
)

// WithMinMaxDelay задаёт min- и max-значения задержки между повторами.
func WithMinMaxDelay(min, max time.Duration) Option {
	return func(cfg *config) {
		cfg.minDelay, cfg.maxDelay = min, max
	}
}

// Этот комментарий не будет включён в документацию. Обе функции
// в документации будут относиться к типу Option, так как возвращают
// значение этого типа.

// WithMultiplier задаёт коэффициент увеличения задержки между повторами.
func WithMultiplier(coef float64) Option {
	return func(cfg *config) {
		cfg.multiplier = coef
	}
}

// DoConstant вызывает функцию типа Operation до тех пор,
// пока она не выполнится без ошибки.
// Задержка между повторами операции фиксирована и определяется delay.
// Общее время выполнения ограничено и определяется timeout.
//
// Deprecated: используйте
//   ctx, cancel := context.WithTimeout(context.Background(), timeout)
//   defer cancel()
//   Do(ctx, WithMinMaxDelay(delay, delay+1), WithMultiplier(1.0)).
func DoConstant(op Operation, delay, timeout time.Duration) error {
	// опустим реализацию
	// ...
	return nil
}

// Do вызывает функцию типа Operation до тех пор, пока она не выполнится без ошибки.
// Задержка между повторами операции увеличивается в соответствии с параметрами
// по умолчанию, которые можно переопределить через opts.
//
// Пример (min: 50ms, max: 500ms, multiplier: 2.0): [50ms, 100ms, 200ms, 400ms].
//
// Повтор прерывается, если:
//
// • для ctx задан deadline и он превышен;
//
// • уровень задержки между повторами превысил значение max.
//
// BUG(Иван Петров): нет валидации входных параметров,
// неверное использование Option может привести к некорректной работе.
//
// BUG(Пётр Иванов): фактически затраченное время может превышать
// ограничение config.MaxDelay, если deadline не задан в ctx.
func Do(ctx context.Context, op Operation, opts ...Option) (retErr error) {
	var retryCnt int
	var doDuration time.Duration
	var opErr error

	defer func() {
		if opErr == nil {
			return
		}
		retErr = fmt.Errorf("операция провалилась после %d попыток (затрачено: %v): %w", retryCnt, doDuration, opErr)
	}()

	cfg := config{minDelay: DefaultMinDelay, maxDelay: DefaultMaxDelay, multiplier: DefaultMultiplier}
	for _, opt := range opts {
		opt(&cfg)
	}

	deadline, deadlineFound := ctx.Deadline()
	for t := cfg.minDelay; t < cfg.maxDelay; t = time.Duration(float64(t) * cfg.multiplier) {
		if deadlineFound && time.Now().After(deadline) {
			opErr = errors.New("истёк срок операции (deadline)")
			return
		}

		if retryCnt > 0 {
			time.Sleep(t)
		}
		if opErr = op(ctx); opErr == nil {
			return
		}

		retryCnt++
		doDuration += t
	}

	return
}
