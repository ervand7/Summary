package some

import (
	"fmt"
	"testing"

	"some/mocks"
)

func TestWithTestifyMock(t *testing.T) {
	mockAbc := &mocks.Abc{}

	param := "Hello"
	testUser := User{param: param, action: mockAbc}

	mockAbc.On("DD", param).Return(nil).Once()

	// call the original logic include mock func
	err := testUser.DoSomething()
	fmt.Println(err)
}
