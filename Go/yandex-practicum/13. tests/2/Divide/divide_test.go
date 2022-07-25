package Divide

import (
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"testing"
)

func TestDivision(t *testing.T) {
	t.Run("ZeroNumerator", func(t *testing.T) {
		result, err := Divide(0, 1)
		require.NoError(t, err)
		assert.Equal(t, 0, result)
	})

	t.Run("BothNonZero", func(t *testing.T) {
		result, err := Divide(4, 2)
		require.NoError(t, err)
		assert.Equal(t, 2, result)
	})

	t.Run("ZeroDenominator", func(t *testing.T) {
		_, err := Divide(1, 0)
		require.Error(t, err)
	})
}
