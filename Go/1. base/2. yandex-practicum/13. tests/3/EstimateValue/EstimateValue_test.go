package EstimateValue

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestEstimateValue(t *testing.T) {
	t.Run("small", func(t *testing.T) {
		result := EstimateValue(0)
		assert.Equal(t, "small", result)
	})

	t.Run("medium", func(t *testing.T) {
		result := EstimateValue(10)
		assert.Equal(t, "medium", result)
	})

	t.Run("big", func(t *testing.T) {
		result := EstimateValue(100)
		assert.Equal(t, "big", result)
	})
}
