package some

import (
	"testing"

	"github.com/golang/mock/gomock"
)

func TestFoo(t *testing.T) {
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()

	m := NewMockFoo(ctrl)

	// Does not make any assertions. Executes the anonymous functions and returns
	// its result when Bar is invoked with 99.
	m.
		EXPECT().
		Bar(gomock.Eq(99)).
		DoAndReturn(func(_ int) int {
			return 101
		}).
		AnyTimes()

	// Does not make any assertions. Returns 101 when Bar is invoked with 99.
	m.
		EXPECT().Bar(99).Return(101).AnyTimes()

	SUT(m)
}
