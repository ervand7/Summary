package Abs

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestAbs(t *testing.T) {
	tests := []struct {
		name  string
		value float64
		want  float64
	}{
		{
			name:  "negative value",
			value: -3.001,
			want:  3.001,
		},
		{
			name:  "small value",
			value: -0.00000001,
			want:  0.00000001,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			v := Abs(tt.value)
			assert.Equal(t, tt.want, v)
		})
	}
}
