package EstimateValue

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestEstimateValueTD(t *testing.T) {
	type args struct {
		value int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "small",
			args: args{
				value: 0,
			},
			want: "small",
		},
		{
			name: "medium",
			args: args{
				value: 10,
			},
			want: "medium",
		},
		{
			name: "big",
			args: args{
				value: 100,
			},
			want: "big",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			assert.Equalf(
				t,
				tt.want,
				EstimateValue(tt.args.value),
				"EstimateValue(%v)",
				tt.args.value,
			)
		})
	}
}
