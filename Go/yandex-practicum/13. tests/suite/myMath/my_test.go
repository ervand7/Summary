package myMath

import (
	"github.com/stretchr/testify/suite"
	"testing"
)

// ExampleTestSuite — это тестовый сьют, который создан путём эмбеддинга suite.Suite.
type ExampleTestSuite struct {
	suite.Suite
	VariableThatShouldStartAtFive int
}

// SetupTest заполняет переменную VariableThatShouldStartAtFive перед началом теста.
func (suite *ExampleTestSuite) SetupTest() {
	suite.VariableThatShouldStartAtFive = 5
}

func (suite *ExampleTestSuite) TestExample() { // все тесты должны начинаться со слова Test
	suite.Equal(5, suite.VariableThatShouldStartAtFive)
}

func TestExampleTestSuite(t *testing.T) {
	// чтобы go test смог запустить сьют, нужно создать обычную тестовую функцию
	// и вызвать в ней suite.Run
	suite.Run(t, new(ExampleTestSuite))
}
