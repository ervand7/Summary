package some

import (
	"errors"
	"math/rand"
	"strconv"
	"testing"
	"time"

	"golang.org/x/sync/errgroup"
)

// слегка оптимизированная функция модуля Abs(-5) == 5,
// которую будем тестировать
func Abs(n int64) int64 {
	y := n >> 63
	return (n ^ y) - y
}

// тестирующая функция запускает 100 проверок
// в отдельных горутинах
func TestAbs(t *testing.T) {
	rand.Seed(time.Now().UnixNano())
	// конструируем группу проверок
	grp := new(errgroup.Group)
	for i := 0; i < 100; i++ {
		// добавляем проверку в группу
		grp.Go(func() error {
			// генерируем псевдослучайное, возможно отрицательное, число
			n := rand.Int63() - 4611686018427387903
			// проверяем корректность Abs
			if Abs(n) != n && Abs(n) != -n {
				// в случае некорректного результата
				// возвращаем число, на котором тест провалился
				return errors.New(strconv.FormatInt(n, 10))
			}
			return nil
		})
	}
	// ожидаем завершения работы группы горутин
	if err := grp.Wait(); err != nil {
		// в случае завершения с ошибкой
		// регистрируем провал теста
		t.Fatal(err.Error())
	}
}
