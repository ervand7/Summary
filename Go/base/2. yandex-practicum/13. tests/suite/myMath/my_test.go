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
func (s *ExampleTestSuite) SetupTest() {
	s.VariableThatShouldStartAtFive = 5
}

func (s *ExampleTestSuite) TestExample() { // все тесты должны начинаться со слова Test
	s.Equal(5, s.VariableThatShouldStartAtFive)
}

func TestExampleTestSuite(t *testing.T) {
	// чтобы go test смог запустить сьют, нужно создать обычную тестовую функцию
	// и вызвать в ней suite.Run
	suite.Run(t, new(ExampleTestSuite))
}
