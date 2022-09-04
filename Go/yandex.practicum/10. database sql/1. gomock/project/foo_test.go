package store

import (
	"github.com/golang/mock/gomock"
	//"project/mocks"
	"testing"
)

// файл persistent/persistent_test.go

func TestGet(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()

	//s := mocks.NewMockFoo(ctrl)

	// гарантируем, что заглушка
	// при вызове с аргументом "Key" вернёт "Value"
	//s.EXPECT().Get("Key").Return([]byte("Value"))

}
