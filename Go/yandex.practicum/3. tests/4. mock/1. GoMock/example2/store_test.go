package some

import (
	"testing"

	"github.com/golang/mock/gomock"
)

func TestGet(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()

	s := NewMockStore(ctrl)
	value := []byte("Some value")

	// гарантируем, что заглушка при вызове с аргументом "Key" вернёт "Value"
	s.EXPECT().Get("Key").Return(
		value, nil,
	).AnyTimes()

	// тестируем функцию
	Lookup(s)
}

// Попробуем стабы:
func TestGet2(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()

	s := NewMockStore(ctrl)
	value := []byte("Some value")

	// при вызове с произвольным аргументом заглушка будет возвращать слайс;
	// метод может быть вызван не более 5 раз
	s.EXPECT().
		Get(gomock.Any()).
		Return(value, nil).
		MaxTimes(5)

	// тестируем функцию
	Lookup(s)
}
