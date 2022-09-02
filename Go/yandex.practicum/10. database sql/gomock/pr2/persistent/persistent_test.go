package persistent

import (
	"github.com/golang/mock/gomock"
	"pr2/store/mocks"
	"testing"
)

func TestGet(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()

	s := mocks.NewMockStore(ctrl)

	// гарантируем, что заглушка
	// при вызове с аргументом "Key" вернёт "Value"
	s.EXPECT().Get("Key").Return([]byte("Value"))

	// тестируем функцию
	//Lookup(s, someCond)
}

/*
Попробуем стабы:
func TestGet(t *testing.T) {
    ctrl := gomock.NewController(t)
    defer ctrl.Finish()

    s := mocks.NewMockStore(ctrl)

    value := []byte("Some value")

    // при вызове с произвольным аргументом
    // заглушка будет возвращать слайс
    // метод может быть вызван не более 5 раз
    s.EXPECT().
    Get(gomock.Any()).
    Return(value, nil).
    MaxTimes(5)

    // тестируем функцию
    Lookup(s, someCond)
}
*/
