package some

import (
	"testing"

	"github.com/golang/mock/gomock"
)

func TestGet(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()

	s := NewMockFoo(ctrl)

	// гарантируем, что заглушка при вызове с аргументом int вернёт int
	s.EXPECT().Do(1).Return(1).AnyTimes()
}
