package Abs

import "testing"

func TestAbs(t *testing.T) {
	type args struct {
		value float64
	}
	tests := []struct {
		name string
		args args
		want float64
	}{
		{
			name: "negative",
			args: args{value: -3},
			want: 3,
		},
		{
			name: "positive",
			args: args{value: 3},
			want: 3,
		},
		{
			name: "negative not zero with small fractional part",
			args: args{value: -2.000001},
			want: 2.000001,
		},
		{
			name: "negative zero with small fractional part",
			args: args{value: -0.000000003},
			want: 0.000000003,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Abs(tt.args.value); got != tt.want {
				t.Errorf("Abs() = %v, want %v", got, tt.want)
			}
		})
	}
}
